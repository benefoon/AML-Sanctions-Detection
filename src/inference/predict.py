import pandas as pd
import joblib

from src.config import MODEL_PATH
from src.preprocessing.clean_data import clean_transaction_data
from src.features.generate_features import generate_basic_features

def predict_from_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Predict sanction risk for each transaction using the trained model.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    df = clean_transaction_data(df)
    df = generate_basic_features(df)

    X = df[["name_length", "is_foreign"]]
    df["sanction_risk"] = model.predict(X)

    return df[["name", "country", "sanction_risk"]]
