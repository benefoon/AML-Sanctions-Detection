import joblib
import os
import time
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=150, class_weight='balanced', random_state=42)
    model.fit(X, y)
    model_path = f"models/artifacts/rf_model_{int(time.time())}.joblib"
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    return model
