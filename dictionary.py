# -*- coding: utf-8 -*-

sozluk = {
        "book" : "kitap",
        "table" : "masa"
        }

print(sozluk)
# anahtar üzerinden gtmemiz gerekiyor..
sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
print(sozluk)


sozluk2 = dict(kitap="book",masa="table")
del(sozluk["book"])
print(len(sozluk))

 