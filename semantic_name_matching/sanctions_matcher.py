import torch
import torch.nn as nn

class SimilarityClassifier(nn.Module):
    def __init__(self, embedding_dim=768):
        super(SimilarityClassifier, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(embedding_dim * 2, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, vec1, vec2):
        combined = torch.cat([vec1, vec2], dim=-1)
        return self.net(combined).squeeze()
