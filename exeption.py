# -*- coding: utf-8 -*-



try:
    sayi=int(input("bir sayi giriniz:"))
        
except:
    print("Hatalı Giriş YAptınız")

print("Devam Ediyor")

#%% 

try:
    sayi=int(input("bir sayi giriniz:"))
        
except ValueError:
    print("Tip Uyuşmazlığı : Lütfen Sayı Giriniz.")
    
except ZeroDivisionError:
    print("Payda Sıfır olamaz")
# şöyleki sayı al hata valueerrorsa bunu yap 
# zero divisoneorrosa bunu yap 
# hiç biri değil ama hata alıyosan excepti yap
    
except:
    print("Hatalı Giriş YAptınız")
    


print("Bitti")

#%%

try:
    sayi=int(input("bir sayi giriniz:"))
# ilk hataysa veya ikinci hataysa bunu yap demek
except (ValueError,ZeroDivisionError): 
    print("Tip Uyuşmazlığı : Lütfen Sayı Giriniz.")
    
except:
    print("Payda Sıfır olamaz")
# şöyleki sayı al hata valueerrorsa bunu yap 
# zero divisoneorrosa bunu yap 
# hiç biri değil ama hata alıyosan excepti yap
    

