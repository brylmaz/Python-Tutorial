# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("insurance.csv")
print(data.columns)

# consola data.describe() yazarsan toplam ne kadar veri var göürsün

# Y EKSENİ
expenses = data.expenses.values.reshape(-1,1)
# X EKSENİ
ageBmis = data.iloc[:,[0,2]].values

regression = LinearRegression()
regression.fit(ageBmis,expenses)# burada verileri doğrusal yaptık


print(regression.predict(np.array([[20,21],[20,22],[20,23],[20,24],[20,25]])))