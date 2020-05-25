# -*- coding: utf-8 -*- 

def veritabanisilmeislemi():
    import sqlite3
    baglan=sqlite3.connect("chinook.db")
    baglan.execute(""" delete from customers where FirstName ='Manoj'
                   
                   """)
    baglan.commit()
    baglan.close()
    
veritabanisilmeislemi()

