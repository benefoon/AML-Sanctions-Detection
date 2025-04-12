import pandas as pd

def generate_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates basic numerical features:
    - Length of name
    - Binary flag for foreign country
    """
    df = df.copy()
    df["name_length"] = df["name"].apply(len)
    df["is_foreign"] = df["country"].apply(lambda c: int(c != "US"))
    return df
