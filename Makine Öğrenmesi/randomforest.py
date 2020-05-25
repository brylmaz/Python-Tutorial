# -*- coding: utf-8 -*-

import numoy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
# aynı Algoritmayı defalarca okutuyoruz


data = pd.read_csv("positions.csv")

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)
#n_estimators=10 ne kadar çok olursa o kadar ayrıntı olur.
regression = RandomForestRegressor(n_estimators=10, random_state=0)
#random_state=0 her seferinde farklı olmasın 
regression.fit(level,salary)

print(regression.predict(8.3))