# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hw_25000.csv")

print(data.columns)

plt.scatter(data.Height,data.Weight)
plt.xlabel("Boy")#grafiğin x kısmının adı
plt.ylabel("Kilo")#grafiğin y kısmının adı
plt.show()