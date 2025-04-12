import pandas as pd

def clean_transaction_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans transaction data by:
    - Dropping nulls in key fields
    - Normalizing name and country fields
    """
    df = df.dropna(subset=["name", "country"]).copy()
    df["name"] = df["name"].astype(str).str.lower().str.strip()
    df["country"] = df["country"].astype(str).str.upper().str.strip()
    return df
