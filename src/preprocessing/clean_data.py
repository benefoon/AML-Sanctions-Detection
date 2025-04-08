import pandas as pd

def clean_transaction_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw transaction data:
    - Drop missing rows
    - Normalize text fields
    """
    df = df.dropna(subset=["name", "country"]).copy()
    df["name"] = df["name"].astype(str).str.lower().str.strip()
    df["country"] = df["country"].astype(str).str.upper().str.strip()
    return df
