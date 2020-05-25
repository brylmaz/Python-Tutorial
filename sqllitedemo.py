# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("chinook.db")
# dtabase dosyasının ismini yanlış yazarsan 
# o isimde database dosyayı oluşutuur

cursor = connection.execute("select * from customers")

for row in cursor:
    print("Fist Name = " + str(+row[0]))


connection.close()

#%%
import sqlite3

connection = sqlite3.connect("chinook.db")
# dtabase dosyasının ismini yanlış yazarsan 
# o isimde database dosyayı oluşutuur

cursor = connection.execute("select FirstName,LastName from customers")

for row in cursor:
    print("Last Name = "+row[1])


connection.close()

# veritabanının en üstünde bulunan satırdaki başlıklar 
# 0 -1 diye gidiyor row ' un içine hangi sayıyı yazarsan
# o satırdaki başlığı çağırırsın

#%%
import sqlite3

connection = sqlite3.connect("chinook.db")
# dtabase dosyasının ismini yanlış yazarsan 
# o isimde database dosyayı oluşutuur

cursor = connection.execute("select FirstName,LastName from customers")

for row in cursor:
    print("Firs Name = " +row[0])
    print("Last Name = "+row[1])
    print("********************")


connection.close()

#%%
import sqlite3

connection = sqlite3.connect("chinook.db")
# dtabase dosyasının ismini yanlış yazarsan 
# o isimde database dosyayı oluşutuur

cursor = connection.execute("select FirstName,LastName from customers where City='Prague' or city='Berlin'")

for row in cursor:
    print("Firs Name = " +row[0])
    print("Last Name = "+row[1])
    print("********************")


connection.close()

#%% VERİLERİ SIRALAMA İŞLEMİ

import sqlite3

connection = sqlite3.connect("chinook.db")
# dtabase dosyasının ismini yanlış yazarsan 
# o isimde database dosyayı oluşutuur

cursor = connection.execute("""select FirstName,LastName 
                            from customers 
                            
                            order by FirstName asc""")
                            #order by FirstName,LastName yazarsan
                            #önce isme göre sırala ismi aynı olanların
                            #soyadına göre sırala
# asc komutu yükselen demek yani A'dan Z'ye
# desc komutu defaultu yani z'den A ya
for row in cursor:
    print("Firs Name = " +row[0])
    print("Last Name = "+row[1])
    print("********************")

# pyhton özel string uzunsa 3 tane tırnak koy bi alt satıra kaydırabilirsin.
connection.close()
