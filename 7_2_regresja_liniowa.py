import numpy as np
import sklearn.linear_model as sl


x = [[0, 1, 2], [5, 1, 5], [15, 2, 7], [25, 5, 5], [35, 11, 13], [45, 15, 12], [55, 34, 45], [60, 35, 12]]
y = [4, 5, 20, 14, 32, 22, 38, 43]

x = np.array(x)
y = np.array(y)
print(x)
print(y)

# oszacowanie wartości parametrów przy x1,x2,x3 - czyli a1,a2,a3 oraz wyrazu wolnego b
liniowy_model_regresji = sl.LinearRegression()
liniowy_model_regresji.fit(x, y)

print("współczynniki a1,a2,a3 modelu regresji liniowej:", liniowy_model_regresji.coef_)
print("wyraz wolny b dla regresji liniowej:", liniowy_model_regresji.intercept_)
# y = 0.45*x1+0.24*x2 + 0.02*x3 + 5.42

R_sq = liniowy_model_regresji.score(x,y)
print("Współczynnik determinacji:",R_sq)

y_prognoza = liniowy_model_regresji.predict([[5, 20, 50]])
print("Prognoza wartości y:", y_prognoza)

y_prognoza_stare = liniowy_model_regresji.predict(x)
print("Prognoza wartości y dla starych danych:", y_prognoza_stare)