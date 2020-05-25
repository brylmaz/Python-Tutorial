# bu "#%%" işaret o kod bloğunu işaretler tablo gibi
# üzerine gelip sağ tıklayıp 
# run cell dersen sadece o işaretli blok çalışır

#%% for range

for x in range(100):#sıfırdan başlar
    print(x+1)
    # 0 dan değilde 1 den başlatmak istersen
    # x+1 yaz
#%%
for x in range(1,10):
    print(x)
    
    
#%%
for x in range(1,10,2):
    # 1 den 10 a kadar 2şer 2şer arttır.
    print(x)
    



#%% For intro
# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir"]

for sehir in sehirler:
    if sehir == "Ankara":
        break # içinde bulunduğu komple kırar.
    print(sehir + " için kod = "+sehir[0:3])
    print("********")
    
    
#%%   
sehirler = ["Ahmet","Mehmet","Hasan"]

for sehir in sehirler:
    if sehir == "Mehmet":
        continue # o anki dönümü yapmaz bir sonraki işleme atlar
    print(sehir + " için kod = "+sehir[0:3])
    print("********")

# bu "#%%" işaret o kod bloğunu işaretler tablo gibi
# üzerine gelip sağ tıklayıp 
# run cell dersen sadece o işaretli blok çalışır
