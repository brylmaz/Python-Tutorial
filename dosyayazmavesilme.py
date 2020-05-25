
f = open("musteriler.txt")

# klasörü kapatcaz babba

f.close()

filetoappend = open("ogrenciler.txt","a")

filetoappend.write("salih""\n""ahmet")
filetoappend.write( "\n" )
filetoappend.write("ahmet")
filetoappend.close()

#%%
import os
if os.path.exists("ogrenciler.txt"): # bu dosya var mı ?
    
    os.remove("ogrenciler.txt")
else:
    print("dosya yok")

os.rmdir("empty") # dosya siler empty dosyasını siler

