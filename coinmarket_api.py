## API CoinMarketCap Data

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
##resp = request.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest')


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'100',
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
    



##json_print(data)


##try:
    ##response = session.get(url,params=parameters)
    ##data = json.loads(response.text)
    ##print(data)
##except (ConnectionError,Timeout,TooManyRedirects) as e:
    ##print(e)
##print(resp.status_code)

