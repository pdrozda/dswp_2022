import pandas as pd
import scipy.stats as scs
import numpy as np

dane_mozg = pd.read_csv('pliki/brain_size.csv', sep=';')
print(dane_mozg.head())

korelacja_pearson, pvalue = scs.pearsonr(dane_mozg['FSIQ'], dane_mozg['VIQ'])
print('Wartość współczynnika korelacji Pearsona:', korelacja_pearson)
print('Wartość poziomu istotności dla korelacji Pearsona:', pvalue)

korelacja_spearman, pvalue = scs.spearmanr(dane_mozg['FSIQ'], dane_mozg['VIQ'])
print('Wartość współczynnika korelacji Spearmana:', korelacja_spearman)
print('Wartość poziomu istotności dla korelacji Spearmana:', pvalue)
if (pvalue>0.05):
    print("korelacja nie zachodzi")
else:
    print("korelacja zachodzi ze współczynnkiem:", korelacja_spearman)

macierz_IQ = [dane_mozg['FSIQ'], dane_mozg['PIQ'], dane_mozg['VIQ'], dane_mozg['MRI_Count']]
macierz_korelacji_IQ = np.corrcoef(macierz_IQ)
print(macierz_korelacji_IQ)
