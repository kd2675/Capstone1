import os
import sys
import urllib.request
import datetime
import time
import json

client_id = '97avHwhY7N2bJ4RysxAx'
client_secret = '74r7XpIXPi'
max_data = 1000
#[CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-client-Id", client_id)
    req.add_header("X-Naver-client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None

#[CODE 2]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" %node
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)     #[CODE 1]

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

#[CODE 3]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description,
                       'org_link':org_link, 'link':org_link, 'pDate':pDate})

    return

#[CODE 0]
def main():
    node = 'news'
    srcText = input('search: ')
    cnt = 0
    jsonResult =[]
    jsonResponse = getNaverSearch(node, srcText, 1, 100) #[CODE 2]
    total = jsonResponse['total']

    #while((jsonResponse != None) and (jsonResponse['display'] != 0)):
    for i in range(0,5):
        for post in jsonResponse['items']:
            cnt+=1
            getPostData(post, jsonResult, cnt) #[CODE3]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100) #[code 2]

    print('all search : %d '%total)

    with open('1)%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)

        outfile.write(jsonFile)
    print("Searching Data : %d" %(cnt))
    print('1)%s_naver_%s.json SAVED' %(srcText, node))

if __name__ == '__main__':
    main()
    
        
