import numpy as np

a = np.array([5, 8, 11])

b = np.array([[5, 8, 11], [6, 9, 45]])

sifir_matrisi = np.zeros((3, 3))

karekok = np.sqrt(a)
logaritma = np.log(a)

ortalama = np.mean(a)
transpoz = np.transpose(b)

eleman_cikar = np.delete(b, 1, axis=0)

import pandas as pd

s = pd.Series([12, 56, 23, 21], index=['a', 'b', 'c', 'd'])

değer_sec = s.iloc[1]

satir_sil = s.drop(['a'])
sutun_sil = s.drop(['b'], axis=0)

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
bilgi = df.info()
istatistikler = df.describe()


print("Numpy Dizi:", a)
print("Sıfır Matrisi:\n", sifir_matrisi)
print("Ortalama:", ortalama)
print("Transpoz:\n", transpoz)
print("Pandas Series:\n", s)
print("Tablo Bilgileri:", bilgi)
print("İstatistikler:\n", istatistikler)