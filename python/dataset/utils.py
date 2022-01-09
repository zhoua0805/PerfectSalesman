import pandas as pd


def parse_csv(csv_path):
    df = pd.read_csv(csv_path)
    print(df.head())
    return


def parse_all(root):
    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]
    data = []
    for month in months:
        parse_csv(f"{root}/{month}.csv")

    return data
