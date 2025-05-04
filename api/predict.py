from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("models/artifacts/latest_model.joblib")

app = FastAPI()

class InputPayload(BaseModel):
    transaction_id: str
    sender_name: str
    receiver_name: str
    amount: float
    currency: str
    timestamp: str

@app.post("/predict")
def predict_transaction(payload: InputPayload):
    try:
        df = pd.DataFrame([payload.dict()])
        # Assume preprocessing pipeline is available
        processed = preprocess_input(df)
        pred = model.predict(processed)[0]
        return {"transaction_id": payload.transaction_id, "prediction": int(pred)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
