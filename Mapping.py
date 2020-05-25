# -*- coding: utf-8 -*-

sayilar = [1,2,3,4,5]

sayilarKareli = []

for sayi in sayilar:
    sayilarKareli.append(sayi*sayi)
    
print(sayilarKareli)

#%%

sayilar = [1,2,3,4,5]

sayilarKareli = list(map(lambda sayi: sayi**2,sayilar))

sayilarKarelii = list(filter(lambda sayi: sayi>2,sayilar))


print(sayilarKarelii)   
print(sayilarKareli)

#%%
sayilar = [1,2,3,4,5]

sayilarKareli = list(map(lambda sayi: sayi**2,sayilar))

sayilarKarelii = list(filter(lambda sayi: sayi>3,sayilar))


print(sayilarKarelii)   
print(sayilarKareli)

from functools import reduce

sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)
#x ile y yi çarp x yaz demek ( x,y:x*y)

print(sayilarFaktoriyel)