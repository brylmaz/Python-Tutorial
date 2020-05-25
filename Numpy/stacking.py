# -*- coding: utf-8 -*-

import numpy as np

a=np.floor(10*np.random.random((2,3)))
# random default olarak 0-1 arası sayı verir
# tam sayı istersek floor ve 10* kulllanırız
b=np.floor(10*np.random.random((2,3)))
print(a,"\n",b)

# vstack diziyi dikey olarak sütun sayısını
# bozmadan altına ekler (vertical dan gelir)
c = np.vstack((a,b))
print(c)
#hstack diziyi yatay olarak satır sayısını
# bozmadan yanına ekler (hertical dan gelir)

d = np.hstack((a,b))
print(d)