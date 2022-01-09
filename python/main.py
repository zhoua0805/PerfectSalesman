import argparse

from model.regression import Regression
import dataset.utils as datautils


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--noise", action='store_true',
                        help="Enable noise in regression")
    parser.add_argument("--data", type=str, help="Path to csv files")
    args = parser.parse_args()
    return args


def main(args):
    # ? Data preprocessing
    X = None
    y = None
    X_test = None

    # ? Regression + profit prediction
    # model = Regression(X, y, args.noise)

    datautils.parse_all(args.data)
    return


if __name__ == '__main__':
    args = parse_args()
    main(args)
