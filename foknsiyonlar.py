# -*- coding: utf-8 -*-

sehir = "Ankara"

print(sehir.upper())
print(sehir.endswith("e"))

#%%

def selamVer(isim):
    print("Merhaba" + isim)
    
selamVer("Engin")
selamVer("Salih")
selamVer("MEhmet")
selamVer("Salih")

#%% defult ayarlar

def selamVer2(isim = "ziyaretçi",soyIsim="arkadaş"):
    print("Merhaba" + isim + soyIsim)
    
selamVer2()
selamVer2("Engin","Demiroğ")
selamVer2("Salih")
selamVer2("MEhmet")
selamVer2("Salih")


