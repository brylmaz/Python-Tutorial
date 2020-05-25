# -*- coding: utf-8 -*-

def joinislemleri():
    import sqlite3
    baglan = sqlite3.connect("chinook.db")
    bla = baglan.execute("""
                   select * from artists inner join albums
                   on artists.ArtistId = albums.ArtistId
                   """)
  # veritabanında execute sql kısmınada yazabiliriz
    for row in bla:
        print("First Name : "+str(row[0]))
        print("Last Name : "+str(row[1]))
        print("******************")
    bla.close()

joinislemleri()    
#%%

def joinislemleri2():
    import sqlite3
    baglan=sqlite3.connect("chinook.db")
    bla = baglan.execute(""" 
                       select albums.Title,artists.Name from artists inner
                       join albums on artists.ArtistId = albums.ArtistId
                         """)
    for row in bla:
        print("First Name : "+row[0])
        print("Last Name : "+row[1])
        print("******************")
    bla.close()

joinislemleri2()    