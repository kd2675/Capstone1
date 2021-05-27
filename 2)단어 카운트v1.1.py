import json
import re
from konlpy.tag import Okt
from collections import Counter





inputFileName = '1)이슈_naver_news'

data = json.loads(open(inputFileName+'.json', 'r', encoding ='utf-8').read())
data

jsonResult =[]
message = ''
for item in data:
    if 'title' in item.keys():
        message = message+re.sub(r'[^\w]',' ',item['title'])+''
nlp = Okt()
message_N = nlp.nouns(message)


count = Counter(message_N)

word_count = dict()
for tag, counts in count.most_common(80):
    if counts < 25:
        tag = " "
    if(len(str(tag))>1):
        word_count[tag] = counts
        print("%s : %d" % (tag,counts))
        jsonResult.append({'title':tag, 'counts':counts})
        


with open('2)%s_search_%s.json' % ('이슈', 'news'), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent = 4, sort_keys = True, ensure_ascii = False)

        outfile.write(jsonFile)
