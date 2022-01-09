import torch.nn as nn


class Model(nn.Module):
    def __init__(self, num_neurons1=12, num_neurons2=6):
        super(Model, self).__init__()
        self.num_neurons1 = 12
        self.num_neurons2 = 6
        # self.batchNorm_fc1 = nn.BatchNorm1d(self.num_neurons1)
        self.fc1 = nn.Linear(18, self.num_neurons1)
        self.fc2 = nn.Linear(self.num_neurons1, self.num_neurons2)
        self.fc3 = nn.Linear(self.num_neurons2, 3)
        self.leaky_relu = nn.LeakyReLU()

    def forward(self, X):
        X = self.leaky_relu(self.fc1(X))
        X = self.leaky_relu(self.fc2(X))
        X = self.fc3(X)

        return X
