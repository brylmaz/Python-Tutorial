def topla(Sayi1,Sayi2):
    return Sayi1+Sayi2

def cikarma(Sayi1,Sayi2):
    return Sayi1-Sayi2

def carpma(Sayi1,Sayi2):
    return Sayi1*Sayi2

def bolme(Sayi1,Sayi2):
    return Sayi1/Sayi2




print("operasyon""\n""1:TOPLA""\n""2:Cikar""\n""3:CARPMA""\n""4:Bolme")

secim = int(input("Hangi İşlemi Yapacaksanız o İşlemi seçiniz : "))
Sayi1 = int(input("Birinci Sayıyı Giriniz : "))
Sayi2 = int(input("İkinci Sayıyı Giriniz :"))

if secim == 1:
    print(topla(Sayi1,Sayi2))
elif secim == 2:
    print(cikarma(Sayi1,Sayi2))
elif secim == 3:
    print(carpma(Sayi1,Sayi2))
elif secim == 4:
    print(bolme(Sayi1,Sayi2))
else:
    print("Yanlış Secim")
    

