## API Integration
## Access db.josn file from https://my-json-server.typicode.com/Shivakoreddi/apiServer01

import json
import csv
import pandas as pd
import requests as rq


resp = rq.get('https://my-json-server.typicode.com/Shivakoreddi/apiServer01/db/')
if resp.status_code==201:
    print("Success")
else:
    print("Failed")
