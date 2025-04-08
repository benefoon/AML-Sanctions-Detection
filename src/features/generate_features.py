import pandas as pd

def generate_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate simple numerical features from transaction data.
    """
    df = df.copy()
    df["name_length"] = df["name"].apply(lambda x: len(x))
    df["is_foreign"] = df["country"].apply(lambda c: int(c != "US"))
    return df
