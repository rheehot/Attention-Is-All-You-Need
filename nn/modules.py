import torch
import torch.nn as nn
import torch.nn.init as init


class Linear(nn.Module):
    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        super(Linear, self).__init__()
        self.linear = nn.Linear(in_features, out_features, bias=bias)
        init.xavier_normal_(self.linear.weight)
        init.zeros_(self.linear.bias)

    def forward(self, inputs):
        return self.linear(inputs)


class LayerNormalization(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super(LayerNormalization, self).__init__()
        self.gamma = nn.Parameter(torch.ones(dim))
        self.beta = nn.Parameter(torch.zeros(dim))
        self.eps = eps

    def forward(self, z):
        mean = z.mean(dim=-1, keepdim=True)
        std = z.std(dim=-1, keepdim=True)
        output = (z - mean) / (std + self.eps)
        output = self.gamma * output + self.beta

        return output
