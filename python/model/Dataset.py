import torch
import torch.utils.data as data


class Dataset(data.Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        X = torch.tensor(self.X[index])
        y = torch.tensor(self.y[index])
        return X, y
