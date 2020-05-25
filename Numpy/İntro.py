# -*- coding: utf-8 -*-
import numpy as np #kütübü çağırırız kısaca np deriz

a = np.arange(15).reshape(3,5)
# 15 elemanlı dizi tanımlarız, boyutu 3 satır 5 sütun
print(a)
print(type(a))
print("Dimension count = " + str(a.ndim))# kaç boyutlu?

b=np.arange(10)
print(b.shape)#kaç boyutlu şekli ne? 10 a 1 lik
print(b.ndim)
