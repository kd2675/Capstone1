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


startDate = "2021-03-01"
endDate = "2021-03-31"
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
            for i in range(len(self.keywordGroups)):
                tmp = pd.DataFrame(result['results'][i]['data'])
                tmp = tmp.rename(columns={'ratio': result['results'][i]['title']})
                df = pd.merge(df, tmp, how='left', on=['period'])
                js = tmp.to_json(orient = 'columns')
                jsonResult.append({'result':js})
            self.df = df.rename(columns={'period': '날짜'})
            
            
        else:
            print("Error Code:" + rescode)
            
        return self.df
    
    """def plot_daily_trend(self):
        
        #일 별 검색어 트렌드 그래프 출력
        
        colList = self.df.columns[1:]
        n_col = len(colList)

        fig = plt.figure(figsize=(12,6))
        plt.title('일 별 검색어 트렌드', size=20, weight='bold')
        for i in range(n_col):
            sns.lineplot(x=self.df['날짜'], y=self.df[colList[i]], label=colList[i])
        plt.legend(loc='upper right')
        
        return fig
    
    def plot_monthly_trend(self):
        
        #월 별 검색어 트렌드 그래프 출력
        
        df = self.df.copy()
        df_0 = df.groupby(by=[df['날짜'].dt.year, df['날짜'].dt.month]).mean().droplevel(0).reset_index().rename(columns={'날짜': '월'})
        df_1 = df.groupby(by=[df['날짜'].dt.year, df['날짜'].dt.month]).mean().droplevel(1).reset_index().rename(columns={'날짜': '년도'})

        df = pd.merge(df_1[['년도']], df_0, how='left', left_index=True, right_index=True)
        df['날짜'] = pd.to_datetime(df[['년도','월']].assign(일=1).rename(columns={"년도": "year", "월":'month','일':'day'}))
        
        colList = df.columns.drop(['날짜','년도','월'])
        n_col = len(colList)
                
        fig = plt.figure(figsize=(12,6))
        plt.title('월 별 검색어 트렌드', size=20, weight='bold')
        for i in range(n_col):
            sns.lineplot(x=df['날짜'], y=df[colList[i]], label=colList[i])
        plt.legend(loc='upper right')
        
        return fig
        return fig_list
        
    """
    
            
        
# 데이터 프레임 정의
naver = NaverDataLabOpenAPI(client_id=client_id, client_secret=client_secret)
jsonResult =[]
inputFileName = '2)이슈_search_news'
data = json.loads(open(inputFileName+'.json', 'r', encoding ='utf-8').read())

message = ''
for item in data:
    if 'title' in item.keys():
        message = message+re.sub(r'[^\w]',' ',item['title'])+''
nlp = Okt()
message_N = nlp.nouns(message)


count = Counter(message_N)


for tag in message_N:
    if tag == '':
        tag = ""
    if(len(str(tag))>1):
        naver = NaverDataLabOpenAPI(client_id=client_id, client_secret=client_secret)
        print("%s" % (tag))
        
        keyword_group_set = {
            'keyword_group_1': {'groupName': tag, 'keywords': [tag]},
        }
        naver.add_keyword_groups(keyword_group_set['keyword_group_1'])
        jsonResult.append({'title':tag})
        df = naver.get_data(startDate, endDate, timeUnit, device, ages, gender)
        
        
with open('3)%s_per_%s.json' % ('이슈', 'news'), 'w', encoding='utf8') as outfile:
    jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)
    outfile.write(jsonFile)




