from pydantic import BaseModel, Field

class TransactionRecord(BaseModel):
    name: str = Field(..., example="John Doe")
    country: str = Field(..., example="US")
    amount: float = Field(..., ge=0.0, example=1000.50)
    currency: str = Field(..., example="USD")
    is_sanctioned: int = Field(..., ge=0, le=1, example=0)  # target
