tupleListe= (2,4,6,"Ankara",(8,9,4))
liste = [2,4,6,"Ankara"]

print(type(tupleListe))
print(type(liste))
print(tupleListe)
print(liste)
print(len(tupleListe))
print(len(liste))

#tuple ile list arasındaki fark nedir

# tuple da veriyi değiştiremiyoruz
# list [0] = 6
# tupleListe [0] = 6
# ctrl+1 ile comment satırı yaapıyoruz
# print(tupleListe[-2])
# print(liste[-2])
# eksili ifadeler dizinin sağından okumaya başlar
# sağdan başlarken 0 dan başlamıyor unutma
print(tupleListe[1:3]) #1den 3 unncu indexe kadar

