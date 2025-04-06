import pandas as pd

def generate_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates basic features such as name length and foreign transaction flag.
    """
    df = df.copy()

    df['name_length'] = df['name'].apply(lambda x: len(str(x)))
    df['is_foreign'] = df['country'].apply(lambda x: 1 if x != 'US' else 0)

    return df
