import argparse

from model.regression import Regression
from model.training import training
import dataset.utils as datautils


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--noise", action='store_true',
                        help="Enable noise in regression")
    parser.add_argument("--data", type=str, help="Path to csv files")
    args = parser.parse_args()
    return args


def main(args):

    # ? Regression + profit prediction
    # training(args.data, epochs=1000, mode='train')
    training(args.data)
    return


if __name__ == '__main__':
    args = parse_args()
    main(args)
