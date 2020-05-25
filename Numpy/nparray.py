# -*- coding: utf-8 -*-
import numpy as np

#a= np.arange(1,10)
a= np.array([1,3,5,7,9,11])
print(a)
print(a.dtype)
#Önemli arrayin içi int sayı olduğu için array komple intdir
#eğer bi tane değeri virgüllü yapsak dizi komple float olur
# veya string olur 
#%%
# -*- coding: utf-8 -*-
import numpy as np

#a= np.arange(1,10)
a= np.array([1,3,5,7,9,11])
# a=a.reshape(2,3) bu da olur 
print(a.reshape(2,3))
print(a)
print(a.dtype)
print(a.ndim)

b=np.array([[1,3],[5,7],[9,11]])
print(b)
print(b.ndim)