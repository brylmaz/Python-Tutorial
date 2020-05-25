import sqlite3

connection = sqlite3.connect("chinook.db")
connection.execute("""insert into customers (firstname,lastname,city,email)
        values ('Barış','YILMAZ','İstanbul','e')""")

connection.commit()
connection.close()

