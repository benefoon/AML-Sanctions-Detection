from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "sample_transactions.csv"
MODEL_PATH = BASE_DIR / "models" / "sanctions_model.pkl"

RANDOM_STATE = 42
TEST_SIZE = 0.2
