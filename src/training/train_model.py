import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

from src.config import DATA_PATH, MODEL_PATH, RANDOM_STATE, TEST_SIZE
from src.preprocessing.clean_data import clean_transaction_data
from src.features.generate_features import generate_basic_features

def train_sanctions_model() -> None:
    """
    Trains a logistic regression model to detect sanctioned transactions.
    Saves the model to disk.
    """
    df = pd.read_csv(DATA_PATH)

    df = clean_transaction_data(df)
    df = generate_basic_features(df)

    if 'is_sanctioned' not in df.columns:
        raise ValueError("Dataset must contain 'is_sanctioned' target column.")

    X = df[['name_length', 'is_foreign']]
    y = df['is_sanctioned']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("Model Evaluation:\n", classification_report(y_test, predictions))

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved at: {MODEL_PATH}")
