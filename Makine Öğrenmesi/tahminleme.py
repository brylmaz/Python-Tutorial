# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #
from sklearn.metrics import r2_score # doğruluk payı ölçme
data = pd.read_csv("hw_25000.csv")

#LinearRegression BU BİR CLASSS
boy = data.Height.values.reshape(-1,1)
kilo = data.Weight.values.reshape(-1,1)
# VERİYİ FİT ETMEDEN ÖNCE YANİ O DÜZ ÇİZGİ YAPMADAN ÖNCE VERİYİ
# 25000 E 1 LİK DURUMA GETİRMEMİZ LAZIM
regression = LinearRegression()
regression.fit(boy,kilo)

print(regression.predict(np.array([[60]]))) #BURADA TAHMİN GÖNDERİYORUZ
print(regression.predict(np.array([[62]]))) #TEK DEĞER YAZDIĞIMIZ İÇİN np.array([[62]])) BÖYLE
print(regression.predict(np.array([[64]]))) #[[70]] BU DA OLUR
print(regression.predict(np.array([[68]])))
print(regression.predict([[70]]))

print(data.columns)

plt.scatter(data.Height,data.Weight) # grafik çizer (x,y)
x = np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red") # BURADA ÇİZGİYİ GÖRELİM DİYE
plt.xlabel("Boy")# x tarafına adı boy
plt.ylabel("Kilo")# y tarafına kilo adı verdik grafik
plt.title("Simple Linear Regression Model")
plt.show() # grafiği göster

print(r2_score(kilo,regression.predict(boy)))# doğrulk payı
# 1 e ne kadar yakınsa o kadardoğru
