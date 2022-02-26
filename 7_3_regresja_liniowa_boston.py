from sklearn import datasets
from statsmodels import api
import pandas as pd

dataset = datasets.load_boston()
print(dataset.DESCR)
print(dataset.feature_names)

dane_X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
dane_Y = pd.DataFrame(dataset.target, columns=['MEDV'])

X = dane_X["RM"]
Y = dane_Y["MEDV"]

X = api.add_constant(X)
print(X)

model_regresji = api.OLS(Y,X).fit()
print(model_regresji.summary())