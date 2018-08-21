#Extracting only the tweet content from the whole json provided by Twitter API

import codecs
from datetime import datetime
import json
import os
import string
import sys
import time
import re
 
inFile = codecs.open('myTweetsFile1.json','r','utf-8')#File that contains json received by twitter
outFile = codecs.open('TweetsOnly3.json','a','utf-8')#file to store output
#i=0
for line in inFile:
    try:
        #i=i+1
        tweet = json.loads(line)
        print("Tweet loaded.")
        #a=[tweet['id'],tweet['text']]
        #outFile.write(str(a))
        outFile.write('{"text":"')
        line=re.sub(r'[\n]', '',str(tweet['text']))
        line=re.sub(r'["]', '',line)
        outFile.write(str(line))
        outFile.write('","id": ')
        outFile.write(str(tweet['id']))
        outFile.write("}"+os.linesep)
        #outFile.write('\n{"created at": ')
        #outFile.write(str(tweet['created_at']))
        #outFile.write(',"userLocation: "')
        #outFile.write(str(tweet['user']['location']))
        #outFile.write(',"userVerified: "')
        #outFile.write(str(tweet['user']['verified']))
        #outFile.write(',"userFollowers: "')
        #outFile.write(str(tweet['user']['followers_count']))
        #outFile.write(',"userTimeZone: "')
        #outFile.write(str(tweet['user']['time_zone']))
        #outFile.write(',"userGeoEnabled: "')
        #outFile.write(str(tweet['user']['geo_enabled']))
        #outFile.write(',"geo: "')
        #outFile.write(str(tweet['geo']))
        #outFile.write(',"coordinates: "')
        #outFile.write(str(tweet['coordinates']))
        #outFile.write(',"place: "')
        #outFile.write(str(tweet['place']))
        #outFile.write(',"filter_level: "')
        #outFile.write(str(tweet['filter_level']))
    except:
        print(sys.exc_info())
#print("Final line count")
#print(i)
