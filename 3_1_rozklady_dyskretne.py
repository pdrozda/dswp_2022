import scipy.stats as scs

p = 0.5 # określenie prawdopodobieństwa sukcesu w rozkładzie bernoulliego oraz dumianowym
date_size = 10000 # wielkość geenerowanego zbioru danych
n = 10 # liczba powtórzeń eksperymentu w rozkładzie dwumianowym
k = 4 # liczba sukcesów w rozkładzie dwumianowym

#rozkład Bernoulliego - jeden eksperyment sukces z prawdopodobieństwem p
rozklad_bernoulliego_dane = scs.bernoulli.rvs(p, size=date_size)
print(rozklad_bernoulliego_dane)
print('Średnia z wygenerowanych danych:', rozklad_bernoulliego_dane.mean())
srednia = scs.bernoulli.stats(p, moments='m')
print('Średnia teoretyczna:', srednia)
sumaPrawdopodobieństw = 0
for i in range(0,n+1):
    prawdopodobienstwoDwumianowy = scs.binom.pmf(i, n, p)
    print(prawdopodobienstwoDwumianowy)
    sumaPrawdopodobieństw = sumaPrawdopodobieństw + prawdopodobienstwoDwumianowy

print(sumaPrawdopodobieństw)