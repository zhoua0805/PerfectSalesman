import torch.nn as nn


class Model(nn.Module):
    def __init__(self, num_neurons1=12, num_neurons2=6):
        super(Model, self).__init__()
        self.num_neurons1 = 12
        self.num_neurons2 = 6
        self.batchNorm_fc1 = nn.BatchNorm1d(15)
        self.batchNorm_fc2 = nn.BatchNorm1d(12)
        self.batchNorm_fc3 = nn.BatchNorm1d(9)
        self.batchNorm_fc4 = nn.BatchNorm1d(6)
        self.fc1 = nn.Linear(18, 15)
        self.fc2 = nn.Linear(15, 12)
        self.fc3 = nn.Linear(12, 9)
        self.fc4 = nn.Linear(9, 6)
        self.fc5 = nn.Linear(6, 3)
        self.leaky_relu = nn.LeakyReLU()
        self.relu = nn.ReLU()

    def forward(self, X):
        X = self.leaky_relu(self.fc1(X))
        X = self.leaky_relu(self.fc2(X))
        X = self.leaky_relu(self.fc3(X))
        X = self.leaky_relu(self.fc4(X))
        # X = self.relu(self.fc1(X))
        # X = self.relu(self.fc2(X))
        X = self.relu(self.fc5(X))

        return X
