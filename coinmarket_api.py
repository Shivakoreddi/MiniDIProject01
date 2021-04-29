## API CoinMarketCap Data

from requests import Request, Session
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
##resp = request.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest')


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'3000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '3cec70c4-edf2-4c94-8d65-d6088d28f342',
}

session = Session()
session.headers.update(headers)



def json_print():
    response = session.get(url,params=parameters)
    return response.json()

#Serializing json data
obj = json_print()
json_obj = json.dumps(obj)

#writing into json file
with open("json files/coin_data.json","w") as file:
    #file.write(json_obj)
    json.dump(obj,file)


    



##json_print(data)


##try:
    ##response = session.get(url,params=parameters)
    ##data = json.loads(response.text)
    ##print(data)
##except (ConnectionError,Timeout,TooManyRedirects) as e:
    ##print(e)
##print(resp.status_code)

