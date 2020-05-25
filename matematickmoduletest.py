
import matematickmodule

matematickmodule.carp(5,4)
matematickmodule.topla(5,4)

#%% bir de şu var

import matematickmodule as mm
mm.carp(3,2)

print(mm.customer["firstname"])

#%% hepsini değilde içindeki bi kısmı alma
from matematickmodule import topla

topla(2,4)
from matematickmodule import customer

print(customer["firstname"])