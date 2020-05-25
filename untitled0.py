# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:05:47 2019

@author: Barış
"""



def hesaplama(deger):
    
    if deger >=85 and deger<=100:
        print("tebrikler AA")
    elif deger>=75 and deger<=85:
        print("tebrikler B")
    elif deger>=65 and deger<75:
        print("tebrikler C")
    elif deger>=55 and deger<65:
        print("tebrikler D")
    elif deger>=45 and deger<55:
        print("tebrikler E")
    elif deger<45:
        print("F")
    else:
        print("hatalı giriş lütfen sayı girin.")


try:
    deger = int(input("notunu gir:"))
    hesaplama(int(deger))   
except:
    print("Tip Uyuşmazlığı : Lütfen Sayı Giriniz.")

