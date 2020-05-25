




def veritabaniguncelleme():
    import sqlite3
    baglan=sqlite3.connect("chinook.db")
    
    baglan.execute(""" update customers set city='İsuuul'
                   where city='İstanbuuuuuul'""")
  #   İstanbuuuuuul yerine isuuul yaz demek
    baglan.commit()
    baglan.close()

veritabaniguncelleme()




