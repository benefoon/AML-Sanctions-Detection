from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_name_embedding(name: str) -> list[float]:
    """
    Converts a name string to a dense numerical embedding
    """
    return _model.encode(name).tolist()
