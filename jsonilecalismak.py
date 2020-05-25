# -*- coding: utf-8 -*-

import json

data = '{"firstname":"engin","lastname":"demirog"}'

y = json.loads(data)

print(y["firstname"])
print(y["lastname"])

#%%
customer = {
        "firstname":"barış",
        "lastname":"yılmaz"    
        
        }

costomerjson = json.dumps(customer)
print(customer)

print(json.dumps("baris"))
