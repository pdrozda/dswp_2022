import numpy as np
import statistics
from scipy import stats as scs

dane_wzrostu = np.loadtxt(r'pliki\Wzrost.csv', delimiter=',')
dane_gielda = np.loadtxt(r'pliki\agt_d.csv', delimiter=',',skiprows =  1, usecols = 1)
dane_wzrostu.sort()
print(dane_wzrostu)
print(dane_gielda)

wzrost_min = dane_wzrostu.min()
wzrost_min_np = np.min(dane_wzrostu)

print("Minimalny wzrost:", wzrost_min)
print("Minimalny wzrost numpy:", wzrost_min_np)

wzrost_max = dane_wzrostu.max()
wzrost_max_np = np.max(dane_wzrostu)

print("maksymalny wzrost:", wzrost_max)
print("maksymalny wzrost numpy:", wzrost_max_np)

wzrost_srednia = dane_wzrostu.mean()
wzrost_srednia_np = np.mean(dane_wzrostu)

print("Średni wzrost:",wzrost_srednia)
print("Średni wzrost numpy:", wzrost_srednia_np)

wzrost_odchylenie = dane_wzrostu.std()
wzrost_odchylenie_np = np.std(dane_wzrostu)
wzrost_odchylenie_statistics = statistics.stdev(dane_wzrostu)
wzrost_odchylenie_statistics_populacja = statistics.pstdev(dane_wzrostu)

print("Odchylenie wzrost:", wzrost_odchylenie)
print("Odchylenie wzrost numpy", wzrost_odchylenie_np)
print("Odchylenie Statistics proba", wzrost_odchylenie_statistics)
print("Odchylenie Statistics populacja", wzrost_odchylenie_statistics_populacja)

wzrost_mediana = np.median(dane_wzrostu)
wzrost_mediana_scipy = scs.scoreatpercentile(dane_wzrostu,50)
wzrost_1_kwartyl_scipy = scs.scoreatpercentile(dane_wzrostu,25)

print("Mediana wzrostu numpy:", wzrost_mediana)
print("Mediana wzrostu scipy:", wzrost_mediana_scipy)
print("Kwartyl wzrostu scipy:", wzrost_1_kwartyl_scipy)

for i in range(1,11):
    print(i, " decyl wzrostu:", scs.scoreatpercentile(dane_wzrostu, i*10))

print("Podstawowe statystyki:", scs.describe(dane_wzrostu))