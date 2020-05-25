# -*- coding: utf-8 -*-

import numpy as np
# 1 den 10 a kadar default olarak 50 sayı üretti
a = np.linspace(1,10)
#print(a)
b = np.linspace(1,10,11)
# 1 den ona kadar 11 tane sayı üret eşit aralıklarla
#print(b)
c = np.linspace(1,5,10)
# 1 den 5 e kadar 10 tane sayı üret eşit aralıklarda
print(c)
#%%
from numpy import pi

x = np.linspace(0,2*pi,100)
# 0 la 360 drece arasında 100 sayı bul eşit aralıklarda
print(x)
print(np.sin(x))
# herbirinin sinüs değerini buluyor

