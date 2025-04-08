from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"

RAW_DATA_PATH = DATA_DIR / "transactions.csv"
MODEL_PATH = MODEL_DIR / "sanctions_classifier.pkl"

RANDOM_SEED = 2025
TEST_SPLIT_RATIO = 0.2
