# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10) #bir dizi oluştur 10 elemanlı 0 dan başlayrak 10 dahil değil
print(a)

b=a
print(a[2])
print(b[2])

b[0]=100
print(a)
print(b)
# --- ÖNEMLİ ---
# FARK ETTİYSEN B Yİ DEĞİŞTİRDİK AMA A DA DEĞİŞTİ
# BUNUN SEBEBİ A=B DEDİĞİN İÇİN NUMPYDA
# İKİSİ AYNI BELLEK GÖZÜNÜ GÖRÜR

# ---PEKİ YA Bİ KOPYASINI ALMAK İSTERSEK?----

c=a.copy()
print(c)
c[0]= 1000
print(a,c)
# c için farkı bi bellek gözü oluşur.

d=a.view()
print("***********")
print(a)
print(d)
d[0]=250
print("***********")
print(a)
print(d)
d.shape=2,5
print("***********")
print(a)
print(d)
a[0]=123
print("***********")
print(a)
print(d)

# BURADA VİEW DE VERİYİ DEĞİŞTİRİRSEN İKİSİNDE 
# DE DEĞİŞİR AMA SATIR SUTUN DEĞİŞTİRİRSEN SADECE O DEĞİŞİR