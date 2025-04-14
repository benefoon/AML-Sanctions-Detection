import json
from pathlib import Path

SANCTIONS_FILE = Path("data/ofac_names.json")

def load_sanctions_names() -> list[str]:
    with open(SANCTIONS_FILE, "r") as f:
        records = json.load(f)
    return [entry["name"] for entry in records]
