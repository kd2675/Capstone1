import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import seaborn as sns

import urllib.request
import datetime
import json
import glob
import sys
import os
import re

from konlpy.tag import Okt
from collections import Counter



import warnings
warnings.filterwarnings(action='ignore')


pd.set_option('display.max_columns', 350)
pd.set_option('display.max_rows', 350)
pd.set_option('display.width', 200)

pd.options.display.float_format = '{:.2f}'.format

client_id = '97avHwhY7N2bJ4RysxAx'
client_secret = '74r7XpIXPi'


startDate = "2021-05-27"
endDate = "2021-05-27"
timeUnit = 'date'
device = ''
ages = []
gender = ''


class NaverDataLabOpenAPI():
    
    #네이버 데이터랩 오픈 API 컨트롤러 클래스
    

    def __init__(self, client_id, client_secret):
        
        #인증키 설정 및 검색어 그룹 초기화
        
        self.client_id = client_id
        self.client_secret = client_secret
        self.keywordGroups = []
        self.url = "https://openapi.naver.com/v1/datalab/search"

    def add_keyword_groups(self, group_dict):
        """
        검색어 그룹 추가
        """

        keyword_gorup = {
            'groupName': group_dict['groupName'],
            'keywords': group_dict['keywords']
        }
        
        self.keywordGroups.append(keyword_gorup)
        print(f">>> Num of keywordGroups: {len(self.keywordGroups)}")
        
    def get_data(self, startDate, endDate, timeUnit, device, ages, gender):
        """
        요청 결과 반환
        timeUnit - 'date', 'week', 'month'
        device - None, 'pc', 'mo'
        ages = [], ['1' ~ '11']
        gender = None, 'm', 'f'
        """

        # Request body
        body = json.dumps({
            "startDate": startDate,
            "endDate": endDate,
            "timeUnit": timeUnit,
            "keywordGroups": self.keywordGroups,
            "device": device,
            "ages": ages,
            "gender": gender
        }, ensure_ascii=False)
        
        # Results
        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id",self.client_id)
        request.add_header("X-Naver-Client-Secret",self.client_secret)
        request.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            # Json Result
            result = json.loads(response.read())
            
            df = pd.DataFrame(result['results'][0]['data'])[['period']]
            ratio=[]
            for i in range(len(self.keywordGroups)):
                for b in result['results'][i]['data']:
                    ratio.append(b['ratio'])
                
            jsonResult.append({'title':tag, 'result':ratio})
            self.df = df
            
            
        else:
            print("Error Code:" + rescode)
            
        return self.df

            
        
# 데이터 프레임 정의
naver = NaverDataLabOpenAPI(client_id=client_id, client_secret=client_secret)
jsonResult =[]
inputFileName = '2)이슈_search_news'
data = json.loads(open(inputFileName+'.json', 'r', encoding ='utf-8').read())

message = ''
for item in data:
    if 'title' in item.keys():
        message = message+re.sub(r'[^\w]'," ",item['title'])+' '
nlp = Okt()
message_N = nlp.nouns(message)
tag1 = ''
for tag in message_N:
    tag1 = tag
for tag in message_N:
    
    if(len(str(tag))>1):
        naver = NaverDataLabOpenAPI(client_id=client_id, client_secret=client_secret)
        print("%s"%(tag))
        
        keyword_group_set = {
            'keyword_group_1': {'groupName': tag1, 'keywords': [tag1]},
            'keyword_group_2': {'groupName': tag, 'keywords': [tag]},
        }
        
        naver.add_keyword_groups(keyword_group_set['keyword_group_1'])
        naver.add_keyword_groups(keyword_group_set['keyword_group_2'])
       
        df = naver.get_data(startDate, endDate, timeUnit, device, ages, gender)
        
        
with open('3)%s_per_%s.json' % ('이슈', 'news'), 'w', encoding='utf8') as outfile:
    jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)
    outfile.write(jsonFile)




