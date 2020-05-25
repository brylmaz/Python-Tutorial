# -*- coding: utf-8 -*-

import pandas as pd


data=[10,20,30,40,50]
df = pd.DataFrame(data)
print(df)

data2 = [["barış","21","istanbul"],["yasemin","18","Ordu"],["efe","25","Konya"]]
df2 = pd.DataFrame(data2,columns=["isim","yaş","şehir"],index=[1,2,3])
print(df2)

print("********************************")
data3 = {"isim":["barış","yasemin","efe"],
         "yaş":[21,18,25],
         "şehir":["istanbul","ordu","konya"]}
df3 = pd.DataFrame(data3,columns=["isim","yaş","şehir"],index=[1,2,3])
print(df3)
print(df3["yaş"])

#del df3["şehir"]
#df3.pop("şehir")
print(df3)

print(df3.loc[2])
print(df3.iloc[1])

df4 = df3.append(df2)
print(df4)
# çok print(df4.head()) fazla veri varsa ilk beş veriyi getirir

print(df4.tail()) # en son 5 veriyi bize getirir. 

