import pandas as pd
import torch
from semantic_models.name_encoder import NameEncoder
from semantic_models.sanctions_matcher import SimilarityClassifier
from semantic_models.utils import load_model, cosine_similarity

def predict_against_sanction_list(input_names, sanction_names, threshold=0.85):
    encoder = NameEncoder()
    model = load_model(SimilarityClassifier(), "models/similarity_classifier.pt")

    encoded_sanctions = [encoder.encode(name) for name in sanction_names]

    results = []
    for name in input_names:
        encoded_name = encoder.encode(name)
        risk = 0
        for s_vec in encoded_sanctions:
            sim_score = cosine_similarity(encoded_name, s_vec)
            if sim_score > threshold:
                risk = 1
                break
        results.append({"name": name, "sanction_risk_semantic": risk})
    return pd.DataFrame(results)
