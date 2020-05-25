# -*- coding: utf-8 -*-

ogrenciler = ["engin","salih","ahmet","mehmet"]

filetoappend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    filetoappend.write(ogrenci)
    filetoappend.write("\n")
filetoappend.close()