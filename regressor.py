from sklearn.ensemble import RandomForestRegressor
from sklearn.base import BaseEstimator
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

class Regressor(BaseEstimator):
    def __init__(self):
        self.clf = RandomForestRegressor(n_estimators=200, max_depth=20, max_features=20)

    def fit(self, X, y):
        self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict(X)
