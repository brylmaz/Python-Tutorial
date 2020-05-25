# -*- coding: utf-8 -*-

import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

c=a-b
d=b**2
e=10* np.sin(a)
# arange 0 dan 4 e kadar array yapar
# 20 den 0 çık - 30 dan 1 çık .... sırasıyla çıkartır
# araylerin eleman sayısı aynı olmalı hata verir

print(e<7)# array olarak true false döner
print(a*b)#elementwise product

print(a@b)#iki şeiyn matris çarpını vercek
print(a.dot(b))#bir üstekiyle aynı

f=np.ones((2,4))
g=np.zeros((2,4))
# 2 ye 4 lük 0 lar ve 2 ye 4 lük 1 ler oluşturdu

h=np.random.random((2,4))
i=np.sum(b)#b deki değerleri toplar
print(np.sum())
k = np.min(b)#b deki minimum mu bul
j = np.max(b)#b deki maxı bul
l= np.sqrt(b) # karekök getirir