import xgboost as xgb
from sklearn.neural_network import MLPClassifier
import numpy as np

class HybridEnsemble:
    def __init__(self):
        self.boost_model = xgb.XGBClassifier(n_estimators=200)
        self.nn_model = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=300)

    def fit(self, X, y):
        self.boost_model.fit(X, y)
        self.nn_model.fit(X, y)

    def predict(self, X):
        pred_boost = self.boost_model.predict_proba(X)[:, 1]
        pred_nn = self.nn_model.predict_proba(X)[:, 1]
        final_pred = (pred_boost + pred_nn) / 2
        return (final_pred > 0.5).astype(int)
