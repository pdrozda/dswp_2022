import statistics as st
import numpy as np
import pandas as pd
from scipy import stats as sc
import matplotlib.pyplot as plt


print("Cwiczenie 1")
url="https://stooq.pl/q/d/l/?s=bos&d1=20100203&d2=20220204&i=w"
data_all=pd.read_csv(url)
data = data_all["Otwarcie"]
print("Maksimum:", data.max())
print("Minimum:", data.min())
print("Mediana:", np.median(data))
print("Mediana high:", st.median_high(data))
print("Mediana low:", st.median_low(data))
print("Średnia:", data.mean())
print("Odchylenie standardowe:", st.stdev(data))
print("Odchylenie standardowe 2:", st.pstdev(data))
print("Wariancja:", st.variance(data))
print("Wariancja 2:", st.pvariance(data))
print("Mode:", st.mode(data))

print()
print("Cwiczenie 2")
data2 = np.loadtxt("pliki/Wzrost.csv", delimiter=',', skiprows=0)

print("Mediana high:", st.median_high(data2))
print("Mediana low:", st.median_low(data2))
print("Odchylenie standardowe:", st.stdev(data2))
print("Odchylenie standardowe 2:", st.pstdev(data2))
print("Wariancja:", st.variance(data2))
print("Wariancja 2:", st.pvariance(data2))
print("Mode:", st.mode(data2))


print()
print("Cwiczenie 3")
print("Kurtosis:", sc.kurtosis(data))
print(sc.describe(data))
print("Skewness:", sc.skew(data))
print("Powtórzenia:", sc.find_repeats(data))
print("Entropy:", sc.entropy(data))
print("Trimmed min:", sc.tmin(data))
print("Trimmed max:", sc.tmax(data))
print("Nth moment:", sc.moment(data))
print("Bayesian confidence intervals  :", sc.bayes_mvs(data))


columns = ["Gender", "FSIQ", "VIQ", "PIQ", "Weight", "Height", "MRI_Count"]
df = pd.read_csv("pliki/brain_size.csv", sep=";", usecols=columns)
print(df.head())
print("Średnia VIQ: ", df["VIQ"].mean())
print("Liczba kobiet: ", df[df.Gender == "Female"].shape)
print("Liczba mężczyzn: ", df[df.Gender == "Male"].shape[0])
plt.hist(df.VIQ)
plt.title("VIQ")
plt.show()
plt.hist(df.PIQ)
plt.title("PIQ")
plt.show()
plt.hist(df.FSIQ)
plt.title("FSIQ")
plt.show()

plt.hist(df[df.Gender == "Female"].VIQ)
plt.title("VIQ kobiety")
plt.show()
plt.hist(df[df.Gender == "Female"].PIQ)
plt.title("PIQ kobiety")
plt.show()
plt.hist(df[df.Gender == "Female"].FSIQ)
plt.title("FSIQ kobiety")
plt.show()