from transformers import AutoTokenizer, AutoModel
import torch

class NameEncoder:
    def __init__(self, model_name="xlm-roberta-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def encode(self, name: str) -> torch.Tensor:
        inputs = self.tokenizer(name, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).squeeze()
