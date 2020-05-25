

import numpy as np

sayilar = np.array([0,5,10,15,20,25,30])

print(sayilar[6]) #6.cı indexi getir
print(sayilar[0:3]) 
print(sayilar[::-1])#diziyi tersten diz
# 2 veya daha fazla boyutlu olursa?

sayilar2 = np.array([[0,5,10],[15,20,25]])
print(sayilar2[1,2])#1 satır 2 .ci index
print(sayilar2[:,2])#tüm satırlardan 2 ci indexi getir
print(sayilar2[:,0:2])#tüm satırlardan 0 ve 1.ci index

print(sayilar2[-1,:])#arrayin son satırını ver veya
print(sayilar2[:,-1])#her satırın sonunu ver














