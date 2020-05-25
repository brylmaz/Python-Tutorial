# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data=np.array(["Engin","Yılmaz","Özgür"])
s = pd.Series(data,index=[1,2,3])
#s = pd.Series(data)
print(s)
print(s[1])

# 

data2={"matematik":10,"fizik":20,"beden":100}
s2 = pd.Series(data2,index=["fizik","matematik","beden"])
print(s2)
# buradaki amaç verilerin yerini değiştirmek 
#istedğimizde verileri koruyarak değişiklik yaparız
print(s2[0])
print(s2["matematik"])

s3 = pd.Series(5,index=[1,2,3,4,5])
print(s3)



