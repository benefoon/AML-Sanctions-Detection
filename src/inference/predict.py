import pandas as pd
import joblib
from src.config import MODEL_PATH
from src.preprocessing.clean_data import clean_transaction_data
from src.features.generate_features import generate_basic_features

def predict_sanction_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Loads the trained model and predicts sanction risk for each transaction.
    Returns the dataframe with predictions.
    """
    model = joblib.load(MODEL_PATH)

    df = clean_transaction_data(df)
    df = generate_basic_features(df)

    features = df[['name_length', 'is_foreign']]
    df['sanction_risk'] = model.predict(features)

    return df[['name', 'country', 'sanction_risk']]
