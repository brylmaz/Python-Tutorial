# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,6)))
# rastgele sayı üret floor 8.3 ise 8 yap
# 5.8 ise 5 yap aşşağı yuvarla demek
print(a)
print(a.shape)
print(a.ravel())# matrisi tek satır yaz
a = a.ravel()
print(a)
print(a.shape)#shape kaç elemanlı demek
# tek satır yazılanı matrise çevir
a = a.reshape(2,9)
print(a)
print(a.T)#transpoz yapar 2,6 dan 6,2 ye çevirir
print(a.reshape(2,-1))

b = a.resize(6,3)
print(b)