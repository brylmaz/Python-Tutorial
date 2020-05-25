
# Faktöriyel Hesaplama
sayi = int(input("Sayi Giriniz : "))
sonuc = 1
if sayi<0:
    print("sıfırdan küçük değerler yazma")
elif sayi>0:
    for x in range(1,sayi+1):
         sonuc*=x 
    print(sonuc)
