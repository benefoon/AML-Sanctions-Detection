import pandas as pd
from pydantic import BaseModel, ValidationError

class TransactionSchema(BaseModel):
    transaction_id: str
    sender_name: str
    receiver_name: str
    amount: float
    currency: str
    timestamp: str

def load_and_validate_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    validated_rows = []
    for _, row in df.iterrows():
        try:
            validated = TransactionSchema(**row.to_dict())
            validated_rows.append(validated.dict())
        except ValidationError as e:
            continue  # Log errors in production
    return pd.DataFrame(validated_rows)
