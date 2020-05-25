
studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet:
        print(student)
    # buyuk kucuk harf duyarlı 
print("derin" in studentsSet)#true ya da False döndürür.
print("Derin" in studentsSet)

if "Derin" in studentsSet:
    print ("Listede var")

#listeye birşey eklenecek ise
studentsSet.add("Ali")
print(studentsSet)


#listin sonuna ekler.
studentsSet.update(["merve","mert","selin"])
print(studentsSet)

#listte kaç eleman var
print(len(studentsSet))

#silme işlemi

studentsSet.remove("selin")
print(len(studentsSet))

# discard birkesdaha silmeye çalışıp bulamayınca hata vermez
studentsSet.discard("selin")
print(len(studentsSet))


# komple listi silme
x = studentsSet.clear()
print(len(studentsSet))
del studentsSet
print(studentsSet)

# set = list
studentsSet2 = set("fatma","hatun","ayse")