#Extracting various fields from the json data received by Twitter API

import codecs
from datetime import datetime
import json
import os
import string
import sys
import time

def parse_json_tweet(line):
    tweet = json.loads(line)
    #print line
    if tweet['lang'] != 'en':
     	#print "non-english tweet:", tweet['lang'], tweet
     	return ['', '', '', [], [], []]

    date = tweet['created_at']
    id = tweet['id']
    nfollowers = tweet['user']['followers_count']
    nfriends = tweet['user']['friends_count']

    if 'retweeted_status' in tweet:
    	text = tweet['retweeted_status']['text']
    else:
    	text = tweet['text']

    hashtags = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    users = [user_mention['screen_name'] for user_mention in tweet['entities']['user_mentions']]
    urls = [url['expanded_url'] for url in tweet['entities']['urls']]
    
    media_urls = []
    if 'media' in tweet['entities']:
	    media_urls = [media['media_url'] for media in tweet['entities']['media']]	    

    return [date, id, text, hashtags, users, urls, media_urls, nfollowers, nfriends]	    
    
# def follow_shortlinks(shortlinks):
#     """Follow redirects in list of shortlinks, return dict of resulting long URLs"""
#     links_followed = {}
#     for shortlink in shortlinks:
#         request_result = requests.get(shortlink)
#         links_followed[shortlink] = request_result.url
#     return links_followed
        
'''start main'''    

inFile = codecs.open('myTweetsFile3.json', 'r', 'utf-8')
fout = codecs.open('FieldTweetsRough.json', 'w', 'utf-8')
	#efficient line-by-line read of big files	
for line in inFile:
	try:
		[tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends] = parse_json_tweet(line)
# 		if not tweet_gmttime: continue
# 		fout.write(line)
 		#"created_at":"Mon Feb 17 14:14:44 +0000 2014"
		try:
			c = time.strptime(tweet_gmttime.replace("+0000",''), '%a %b %d %H:%M:%S %Y')
		except: 
			print ("pb with tweet_gmttime", tweet_gmttime, line)
			pass	
		tweet_unixtime = int(time.mktime(c))
#		fout.write(line)
		fout.write(str([tweet_unixtime, tweet_gmttime, tweet_id, text, hashtags, users, urls, media_urls, nfollowers, nfriends]) + "\n")
	except: 
			#print "pb with tweet:", line
#			print sys.exc_info()[0], line
		pass
 #file_timeordered_json_tweets.close()
 #fout.close()
