from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd

from inference.predict import predict_from_transactions

app = FastAPI(title="AML Sanctions Detection API", version="1.0")

class TransactionInput(BaseModel):
    name: str = Field(..., example="Ali Reza")
    country: str = Field(..., example="IR")

@app.post("/predict/", summary="Predict sanction risk for a transaction")
def predict(transaction: TransactionInput):
    df = pd.DataFrame([transaction.dict()])
    result = predict_from_transactions(df)
    return result.to_dict(orient="records")[0]
