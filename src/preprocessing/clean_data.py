import pandas as pd

def clean_transaction_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic data cleaning: removes missing values, trims and lowers string fields.
    """
    df = df.copy()
    df.dropna(inplace=True)

    if 'name' in df.columns:
        df['name'] = df['name'].astype(str).str.lower().str.strip()

    if 'country' in df.columns:
        df['country'] = df['country'].astype(str).str.upper().str.strip()

    return df
