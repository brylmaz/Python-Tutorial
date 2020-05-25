# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir"]

for sehir in sehirler:
    if sehir == "Ankara":
        break # içinde bulunduğu komple kırar.
    print(sehir + " için kod = "+sehir[0:3])
    print("********")
    
    
    
sehirler = ["Ahmet","Mehmet","Hasan"]

for sehir in sehirler:
    if sehir == "Mehmet":
        continue # o anki dönümü yapmaz bir sonraki işleme atlar
    print(sehir + " için kod = "+sehir[0:3])
    print("********")