#Coin data

##import coinmarket_api as ca
import pandas as pd
import json

with open("json files/coin_data.json","r") as file:
    obj = json.load(file)
    coin_df = obj['data']

##d = pd.DataFrame(obj['data'],columns = ['id','cmc_rank','name','symbol','max_supply','quote'])
##d = pd.DataFrame.from_dict(obj['data'])
header = "coins"
line = {}
for i in range(10):
    line[i] = str(coin_df[i])
    print(line[i])




def display_coin(obj):
    d= {}
    i = 0
    c = {}
    key = "data"
    c.setdefault(key,[])
    while i<=10:
        for coin in obj['data']:
            d['id'] = coin['id']
            d['cmc_rank'] = coin['cmc_rank']
            d['name'] = coin['name']
            d['price'] = coin['quote']['USD']['price']
            d['percent_change_24h']  = coin['quote']['USD']['percent_change_24h']
            d['percent_change_7d'] = coin['quote']['USD']['percent_change_7d']
            d['percent_change_30d'] = coin['quote']['USD']['percent_change_30d']
            d['max_supply'] = coin['max_supply']
            c[key].append(d)
        i=i+1
        return c
l = display_coin(obj)



