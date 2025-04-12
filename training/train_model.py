import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

from config import DATA_PATH, MODEL_PATH, RANDOM_STATE, TEST_SIZE
from preprocessing.clean_data import clean_transaction_data
from features.generate_features import generate_basic_features

def train_sanctions_model() -> None:
    """
    Loads data, preprocesses, trains a model, and saves it to disk.
    """
    df = pd.read_csv(DATA_PATH)

    if "is_sanctioned" not in df.columns:
        raise ValueError("Missing 'is_sanctioned' target column.")

    df = clean_transaction_data(df)
    df = generate_basic_features(df)

    X = df[["name_length", "is_foreign"]]
    y = df["is_sanctioned"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    model = LogisticRegression(max_iter=200, random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Model Evaluation:")
    print(classification_report(y_test, y_pred))

    joblib.dump(model, MODEL_PATH)
    print(f"✔ Model saved to: {MODEL_PATH}")
