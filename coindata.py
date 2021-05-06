#Coin data

##import coinmarket_api as ca
import pandas as pd
import json

with open("json files/coin_data.json","r") as file:
    obj = json.load(file)
    coin_df = obj['data']

##d = pd.DataFrame(obj['data'],columns = ['id','cmc_rank','name','symbol','max_supply','quote'])
##d = pd.DataFrame.from_dict(obj['data'])

##line.setdefault(header,[])


def display_coin(obj):
    d= {}
    i = 0
    c={}
    key = "data"
    c.setdefault(key,[])
    for coin in coin_df:
        d[i] = {'id': coin['id'],'cmc_rank': coin['cmc_rank'],'name': coin['name'],'price':coin['quote']['USD']['price'],'percent_change_24h':coin['quote']['USD']['percent_change_24h'],'percent_change_7d':coin['quote']['USD']['percent_change_7d'],'percent_change_30d':coin['quote']['USD']['percent_change_30d'],'max_supply':coin['max_supply']}
        c[key].append(d[i])
        ##df = pd.DataFrame(data=d[i],index='id')

    return c
print(display_coin(obj))



