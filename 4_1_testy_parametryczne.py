import numpy as np
import scipy.stats as scs

m = 168
dane_wzrost = np.loadtxt('pliki/Wzrost.csv', delimiter=',')
dane_wzrost1 = np.loadtxt('pliki/Wzrost1.csv', delimiter=',')


print('Srednia wzrostu:', dane_wzrost.mean())

#Test dla 1 średniej
# jeśli wartość pvalue jest większa od zakładanego poziomu błędu np. 0,05 to przyjmujemy H0
# jeśli wartość pvalue jest mniejsza od zakładanego poziomu błędu np. 0,05 to odrzucamy H0, przyjmujemy H1
test_1_srednia = scs.ttest_1samp(dane_wzrost, m)
print('Test dla jednej średniej (wartość statystyki, prawdopodobieństwo):', test_1_srednia)

# Test dla 2 średnich - próby niezależne
print('Srednia wzrostu:', dane_wzrost.mean())
print('Srednia wzrostu1:', dane_wzrost1.mean())
test_2_niezalezne = scs.ttest_ind(dane_wzrost, dane_wzrost1)
print('Test dla 2 średnich, próby niezależne:', test_2_niezalezne)

# Test dla 2 średnich próby zależne
test_2_zalezne = scs.ttest_rel(dane_wzrost, dane_wzrost1)
print('Test dla 2 średnich, próby zależne:', test_2_zalezne)
test_2_zalezne_1 = scs.ttest_1samp(dane_wzrost-dane_wzrost1,0)
print('Test dla 2 średnich, próby zależne, drugi sposób:', test_2_zalezne_1)