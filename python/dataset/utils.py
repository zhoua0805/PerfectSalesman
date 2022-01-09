import pandas as pd


def parse_csv(csv_path):
    df = pd.read_csv(csv_path)
    # df = df[df['Quantity'] > 0]
    onehotdf = pd.get_dummies(df['Sub-Category'])
    X = pd.concat([df['Discount'], onehotdf], axis=1)
    y = df[['Sales', 'Quantity', 'Profit']]

    return X.to_numpy(), y.to_numpy()


def parse_all(root):
    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]
    data = []
    for month in months:
        X, y = parse_csv(f"{root}/{month}.csv")
        data.append((X, y))
        print(X.shape, y.shape)

    return months, data
