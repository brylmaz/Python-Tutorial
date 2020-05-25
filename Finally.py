# -*- coding: utf-8 -*-

import sys #♠ hata döndürme kütübü
liste = [7,'baris',0,3,"6"]

for x in liste:
    try:
        print("sayi: " + str(x))
        sonuc = 1/int(x)
        print("Sonuç : " + str(sonuc))
    except ValueError:
        print(str(x)+"bir sayı değil")
    except ZeroDivisionError:
        print(str(x) + "sıfıra bölme hatası")
    except:
        print(str(x) + "Hesaplanamadı")
        print("sistem Diyor ki : " + str(sys.exc_info()[0]))
    finally 
        print("bitti")
# finally her türlü çalışacak bloktur mesela bi dosyayı kapatmayı unuttuk 
        # bu komutla kapatırız örneğin
#   str(sys.exc_info()[0] hatayı görmek için 0 
# yazılmasının sebebi ilk kelimeyi getir demek  