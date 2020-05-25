# -*- coding: utf-8 -*-
# for döngüsüün çalışma mantığını bilelim
# sıralı işlemlerde kullanılır

sehirler = ["İzmir","İstanbul","Ankara"]

iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
#For un mantığı 
for sehir in sehirler:
    print(sehir)
