# -*- coding: utf-8 -*-

# "w" write dan gelir dosyaya yaz demek
# "r" read ten gelir oku demek
# "a" append den geliyor dosyayı okucam aynı zamanda ekleme yapıcam yoksa oluşturcam
# "x" create dosyayı oluştur demek aynı dosyadan olulturamassın


f = open("musteriler.txt")

#print(f.read())

# read(10) yazarsan ilk 10 karakteri oku demek

#%% readline satır satır okur tabi sırayla

f = open("musteriler.txt")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

#%% döngülerle satır satır okuturuz
f = open("musteriler.txt")
for x in f:
    print(x)