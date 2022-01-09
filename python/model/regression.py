import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.multioutput import MultiOutputRegressor


class Regression():
    def __init__(self, X, y, noise):
        self.X = X
        self.noise = np.random.normal(
            0, 1e-3, (1000, 3)) if noise == True else 0
        self.y = y + self.noise

    def train(self):
        self.model = MultiOutputRegressor(
            xgb.XGBRegressor(objective='reg:squarederror')).fit(self.X, self.y)

    def __call__(self, X):
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        return np.mean((self(X_test) - y_test)**2, axis=0)


# def regression(noise):
#     # get some noised linear data
#     X = np.random.random((1000, 18))
#     a = np.random.random((18, 3))
#     n = np.random.normal(0, 1e-3, (1000, 3)) if noise == True else 0
#     y = np.dot(X, a) + n

#     # fitting
#     multioutputregressor = MultiOutputRegressor(
#         xgb.XGBRegressor(objective='reg:squarederror')).fit(X, y)

#     return multioutputregressor
