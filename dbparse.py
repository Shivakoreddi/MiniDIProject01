##Db.json data parsing

import API as ap
import json


def json_print(obj):
    #create formated json data into object
    text = json.dumps(obj,sort_keys=True,indent=4)
    print(text)

obj= ap.respond()['data']

json_print(obj)

ID = []
for d in obj:
    id = d['ID Year']
    ID.append(id)

print(ID)
