#Rough file for clustering

import sys
import json
import re
import codecs
import os

f=codecs.open('myTweetsFile1.json','r','utf-8')
i=0
for line in f:
    try:
        tweet = json.loads(str(line))
        id=tweet['id']
        print(id)
        text=tweet['text']
        #print(text)
        #url = re.search(r"http\S+", "",text)
        #print(url)
        print("I am bee, I drink tea")
        for temp in range(0,i+1):
           clus = codecs.open('t'+str(temp)+'.json','a+','utf-8')
           print("Second file open")
           for data in clus:
               print("heyl")
               print(data)
               tweet1=json.loads(data)
               print("Data loaded")
               if id==tweet1['id']:
                   clus.write(str(tweet))
                   break;
               #elif url==re.search(r"http\S+","",tweet1['text']):
                #   clu.write(tweet)
                 #  break;
               else:
                   print("hello")
                   f1=codecs.open('t'+str(++i)+'.json','a','utf-8')
                   f1.write(str(tweet))
                   f1.close()
    except BaseException:
        print(sys.exc_info())
f.close()
