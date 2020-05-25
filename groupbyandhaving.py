# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.execute("""select city,count(*) from Customers 
                            group by city
                            order by count(*) desc""")
#order by her zaman sorgunun sonuna yazılır.
for row in cursor:
    print("city = " +str(row[0]))
    print("Last Name = "+str(row[1]))
    print("********************")
connection.close()

#%% 
import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.execute("""select city,count(*) from Customers 
                            group by city having count(*)>1
                            order by count(*) desc""")
#order by her zaman sorgunun sonuna yazılır.
for row in cursor:
    print("city = " +row[0])
    print("Last Name = "+str(row[1]))
    print("********************")
connection.close()