import pandas as pd
import torch
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from deep_models.model_builder import SanctionsNet
from deep_models.utils import save_model, EarlyStopping
from config import DATA_PATH, RANDOM_STATE

def train_deep_model():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=["name", "country", "is_sanctioned"]).copy()

    df["name_length"] = df["name"].apply(lambda x: len(str(x)))
    df["is_foreign"] = df["country"].apply(lambda c: int(str(c).upper() != "US"))

    features = df[["name_length", "is_foreign"]].values
    labels = df["is_sanctioned"].values.reshape(-1, 1)

    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    X_train, X_val, y_train, y_val = train_test_split(features, labels, test_size=0.2, random_state=RANDOM_STATE)

    train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32),
                                  torch.tensor(y_train, dtype=torch.float32))
    val_dataset = TensorDataset(torch.tensor(X_val, dtype=torch.float32),
                                torch.tensor(y_val, dtype=torch.float32))

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32)

    model = SanctionsNet(input_dim=features.shape[1])
    criterion = torch.nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    early_stopper = EarlyStopping(patience=5)

    for epoch in range(50):
        model.train()
        for x_batch, y_batch in train_loader:
            optimizer.zero_grad()
            preds = model(x_batch).squeeze()
            loss = criterion(preds, y_batch.squeeze())
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_loss = 0
            for x_batch, y_batch in val_loader:
                preds = model(x_batch).squeeze()
                val_loss += criterion(preds, y_batch.squeeze()).item()
            avg_val_loss = val_loss / len(val_loader)

        print(f"Epoch {epoch+1}, Val Loss: {avg_val_loss:.4f}")
        if early_stopper.step(avg_val_loss):
            print("🔕 Early stopping triggered.")
            break

    save_model(model, "models/dl_sanctions_model.pt")
    print("✅ Deep model saved.")

if __name__ == "__main__":
    train_deep_model()
