import pandas as pd

def add_amount_bucket(df: pd.DataFrame) -> pd.DataFrame:
    df['amount_bucket'] = pd.cut(df['amount'], bins=[0, 1000, 10000, 50000, float('inf')], labels=["low", "medium", "high", "very_high"])
    return df

def create_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    df = add_amount_bucket(df)
    df['is_foreign_currency'] = df['currency'].apply(lambda x: int(x != 'USD'))
    df['hour_of_day'] = pd.to_datetime(df['timestamp']).dt.hour
    return df
