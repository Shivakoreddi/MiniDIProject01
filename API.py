## API Integration
## Access db.josn file from https://my-json-server.typicode.com/Shivakoreddi/apiServer01

import json
import csv
import pandas as pd
import requests as rq

def respond():
    resp = rq.get('https://my-json-server.typicode.com/Shivakoreddi/apiServer01/db/')
    if resp.status_code==200:
        return resp.json()
    else:
        return resp.status_code
##print(resp.status_code)
##print(resp.json())

def json_print(obj):
    #create formated json data into object
    text = json.dumps(obj,sort_keys=True,indent=4)
    return text

json_print(resp.json())



    
