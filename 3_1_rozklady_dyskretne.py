import scipy.stats as scs

p = 0.5 # określenie prawdopodobieństwa sukcesu w rozkładzie bernoulliego oraz dumianowym
date_size = 100000000 # wielkość geenerowanego zbioru danych

rozklad_bernoulliego_dane = scs.bernoulli.rvs(p, size=date_size)
print(rozklad_bernoulliego_dane)
print('Średnia z wygenerowanych danych:', rozklad_bernoulliego_dane.mean())
srednia = scs.bernoulli.stats(p, moments='m')
print('Średnia teoretyczna:', srednia)