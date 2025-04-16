import torch
import pandas as pd
from sklearn.preprocessing import StandardScaler
from deep_models.model_builder import SanctionsNet
from deep_models.utils import load_model

def predict_with_deep_model(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["name", "country"]).copy()

    df["name_length"] = df["name"].astype(str).apply(len)
    df["is_foreign"] = df["country"].astype(str).str.upper().apply(lambda c: int(c != "US"))

    X = df[["name_length", "is_foreign"]].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = SanctionsNet(input_dim=X.shape[1])
    model = load_model(model, "models/dl_sanctions_model.pt")
    model.eval()

    inputs = torch.tensor(X_scaled, dtype=torch.float32)
    with torch.no_grad():
        outputs = model(inputs).squeeze().numpy()

    df["sanction_risk_dl"] = (outputs > 0.5).astype(int)
    return df[["name", "country", "sanction_risk_dl"]]
