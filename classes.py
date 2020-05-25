class Matematik:
    
    def __init__(self): # burası ilk clasın çalıştığını anlamak için
        print("Çalıştı")
    
    def topla(self,sayi1,sayi2):
        return sayi1+sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1-sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1*sayi2

    def bol(self,sayi1,sayi2):
        return sayi1/sayi2
    

matematik = Matematik()
matematik2 = Matematik()

print("Toplam = "   +   str(matematik.topla(2,78)))

#%% bir farklısı ama aynısı
class Matematik:
    
    def __init__(self,sayi1,sayi2): # burası ilk clasın çalıştığını anlamak için
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    
    def topla(self):
        return self.sayi1+self.sayi2
    
    def cikar(self):
        return self.sayi1-self.sayi2
    
    def carp(self):
        return self.sayi1*self.sayi2

    def bol(self):
        return self.sayi1/self.sayi2
    

matematik = Matematik(2,78)
matematik2 = Matematik(3,60)

print("Toplam = "   +   str(matematik.topla()))

#%% classta özelik tutma
class person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
        
person1 = person("Barış","Yılmaz",26)
print(person1.age)
 
#%% inheritance miras kavramı
class person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
        
person1 = person("Barış","Yılmaz",26)
print(person1.age)

class calisan(person):
    def __init__(self,salary):
        self,salary = salary
    
class musteri(person):
    def __init__(self,creditcardnumber):
        self.creditcardnumber = creditcardnumber
        
ahmet = calisan()
mehmet = musteri()



























