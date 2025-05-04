from fastapi.testclient import TestClient
from api.predict import app

client = TestClient(app)

def test_prediction_endpoint():
    payload = {
        "transaction_id": "TX1001",
        "sender_name": "Ali Corp",
        "receiver_name": "Zara Inc",
        "amount": 45000,
        "currency": "USD",
        "timestamp": "2025-01-01T12:00:00Z"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
