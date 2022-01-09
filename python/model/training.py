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
    # optimizer = optim.SGD(model.parameters(), lr=lr)

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

    return


def training(root, epochs=100, batchsize=16, lr=0.001, mode='eval'):
    torch.manual_seed(10)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device being used: {device}")

    months, data = parse_all(root)
    datasets = [Dataset(X, y) for X, y in data]

    if mode == 'train':
        # ? Dataloaders for training
        trainloaders = [DataLoader(
            dataset, batch_size=batchsize, shuffle=True, drop_last=True) for dataset in datasets]

        for i, trainloader in enumerate(trainloaders):
            month = months[i]
            print(f"Training loop for month: {month}")
            training_helper(device, trainloader, lr,
                            epochs, f"{root}/{month}.pt")

            break

    else:
        # ? Evaluation
        valloaders = [DataLoader(
            dataset, batch_size=len(dataset), shuffle=True, drop_last=True) for dataset in datasets]
        for j, valloader in enumerate(valloaders):
            month = months[j]
            print(f"Evaluating month: {month}")
            model = Model()
            model.load_state_dict(torch.load(f"{root}/{month}.pt"))
            model = model.to(device)

            for data, label in valloader:
                data = data.to(device)
                label = label.to(device)
                output = model(data)

                loss = torch.mean(torch.square(label - output), dim=0)
                print(loss)

            break
    return
