import scipy.stats as scs

print('Zadanie 1:')
elements = (1,2,3,4,5,6)
probabilities = (1/6,1/6,1/6,1/6,1/6,1/6)
data = scs.rv_discrete(values=(elements,probabilities))
print('Średnia:', data.mean())
print('Mediana:', data.median())
print('Odchylenie standardowe:', data.std())
print('Wartość oczekiwana:', data.expect())

print()
print('Zadanie 2:')
k=3
n=10
p = 0.4
data_size = 1000000
bernoulli = scs.bernoulli.rvs(p, size=data_size)
binomial = scs.binom.rvs(n,p,size=data_size)
poisson = scs.poisson.rvs(k,size=data_size)


srednia, wariancja, skosnosc, kurtoza = scs.bernoulli.stats(p, moments='mvsk')
print('Średnia Bernoulli:', bernoulli.mean())
print('Średnia teoretyczna Bernoulli:', srednia)
print('Wariancja Bernoulli:', bernoulli.var())
print('Wariancja teoretyczna Bernoulli:', wariancja)
print('Kurtoza Bernoulli:', scs.kurtosis(bernoulli))
print('Kurtoza teoretyczna Bernoulli:', kurtoza)
print('Skośność Bernoulli:', scs.skew(bernoulli))
print('Skośność teoretyczna Bernoulli:', skosnosc)


print('Średnia binomial:', binomial.mean())
print('Odchylenie binomial:', binomial.std())
print('Kurtoza binomial:', scs.kurtosis(binomial))
print('Skośność binomial:', scs.skew(binomial))

print('Średnia poisson:', poisson.mean())
print('Odchylenie poisson:', poisson.std())
print('Kurtoza poisson:', scs.kurtosis(poisson))
print('Skośność poisson:', scs.skew(poisson))