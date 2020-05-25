# -*- coding: utf-8 -*-

        # kümeler gibi #
        
        
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}
# aynı elemanları bidaha yazmaz
print(setA | setB)
print(setA.union(setB)) # terside olur.

# bu da ortak elemanları gösterir.
print(setA & setB)
print(setA.intersection(setB)) # terside olur.

# kümeler arası fark için
print(setA -setB)
print(setA.difference(setB))#yer değiştirebilir. 


print(setA ^ setB)
print(setA.symmetric_difference(setB))