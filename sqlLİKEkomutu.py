# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.execute("""select FirstName,LastName from Customers 
                            where FirsName like '%a%'""")
# %a% kelimenin içinde a varmı
# a% kelimenin başı a mı?
# %a kelimenin sonu a mı?
# % nin anlamı ondan sonrasını siktir et demek
#order by her zaman sorgunun sonuna yazılır.
for row in cursor:
    print("city = " +row[0])
    print("Last Name = "+str(row[1]))
    print("********************")
connection.close()