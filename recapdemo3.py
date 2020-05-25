# -*- coding: utf-8 -*-

sayi = int(input("Sayi Giriniz : "))

asalmi = True
for x in range(2,sayi):
    if (sayi % x) ==0:
        asalmi = False
        break
if asalmi:
    print("ASAL")
else:
    print("ASAL DEĞİL")

