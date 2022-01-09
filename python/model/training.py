import torch
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim

from .Model import Model
from .Dataset import Dataset
from dataset.utils import parse_all


def training_helper(device, dataloader, lr, epochs, save_path):
    # ? Run the training loop for each dataloader

    # ? Instantiate model, optimizer and loss function
    model = Model()
    model = model.to(device)
    loss_fn = nn.MSELoss()
    optimizer = optim.AdamW(model.parameters(), lr=lr)

    for epoch in range(epochs):
        for data, label in dataloader:
            optimizer.zero_grad()
            data = data.to(device)
            output = model(data)

            # ? Backprop
            label = label.to(device)
            loss = loss_fn(input=output, target=label)
            loss.backward()
            optimizer.step()

    torch.save(model.state_dict(), save_path)
    # model = model.to(torch.device('cpu'))

    return loss.item()


def training(root, epochs=100, batchsize=16, lr=0.001):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device being used for training: {device}")

    # ? Dataloaders
    months, data = parse_all(root)
    datasets = [Dataset(X, y) for X, y in data]
    dataloaders = [DataLoader(
        dataset, batch_size=batchsize, shuffle=True) for dataset in datasets]

    for i, dataloader in enumerate(dataloaders):
        month = months[i]
        print(f"Training loop for month: {month}")
        loss = training_helper(device, dataloader, lr,
                               epochs, f"{root}/{month}.pt")
        print(f"Loss: {loss}")

    return
