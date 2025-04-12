import pandas as pd
import joblib

from config import MODEL_PATH
from preprocessing.clean_data import clean_transaction_data
from features.generate_features import generate_basic_features

def predict_from_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Uses the trained model to predict sanction risk on incoming transactions.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    df = clean_transaction_data(df)
    df = generate_basic_features(df)

    X = df[["name_length", "is_foreign"]]
    df["sanction_risk"] = model.predict(X)

    return df[["name", "country", "sanction_risk"]]
