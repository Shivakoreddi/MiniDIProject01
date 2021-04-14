#Coin data

import coinmarket_api as ca
import pandas as pd

coin = []

obj = ca.json_print()
##print(type(obj))


d = pd.DataFrame(obj['data'],columns = ['id','cmc_rank','name','symbol','max_supply',])
print(d)

for i in obj['data']:
    id = i['name']
    
    coin.append(id)

print(coin)
