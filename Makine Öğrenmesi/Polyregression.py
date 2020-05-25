# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


data = pd.read_csv("positions.csv")
print(data.columns)

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)

regression = LinearRegression()
regression.fit(level,salary) # fitliyoruz 

tahmin = regression.predict(8.3)# 8.3 ü tahmin et 

plt.scatter(level,salary,color="red")
plt.plot(level,regression.predict(level),color="blue")
plt.show()

regressionPoly = PolynomialFeatures(degree = 4 )# ayrıntılı seviye
# polinom oldugunu anlatmamız lazım
levelPoly = regressionPoly.fit_transform(level)
levelPoly2 = regressionPoly.fit_transform(salary)
regression2 = LinearRegression()
regression2.fit(levelPoly,levelPoly2)

tahmin2 = regression2.predict(regressionPoly.fit_transform(8.3))


plt.scatter(level,salary,color="red")
plt.plot(level,regression.predict(level),color="blue")
plt.plot(level,regression2.predict(levelPoly))
plt.show()


