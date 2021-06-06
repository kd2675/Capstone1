import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re
import json
from datetime import datetime

client_id = 'kO0rlKQibESYwzGjrEKc'
client_secret = 'eGEbxpdZbD'

url = "https://openapi.naver.com/v1/datalab/search"

body = {"startDate": "2020-01-01",
        "endDate": "2021-05-13",
        "timeUnit": "month",
        "keywordGroups": [{"groupName": "음식",
                           "keywords": ["수박", "watermelon"]}],
        "device": "pc", "ages": ["1", "2"]}
body = json.dumps(body, )


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
request.add_header("Content-Type", "application/json")

response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    scraped = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

result = json.loads(scraped)


data = result['results'][0]['data']

time = [pd.to_datetime(i['period']) for i in data]

value = [i['ratio'] for i in data]

data = pd.DataFrame({'Time': time, 'Trend_idx': value})
print(data)