#Streaming tweets from Twitter and storing the json response by Twitter API in file

import csv
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
print("Imports successful")
#Enter following data for accessing Twitter API.
ckey=''
csecret=''
atoken=''
asecret=''
print("Keys set successfully")

class listener(StreamListener):
    #i=0
    #j=0
    def on_data(self, data):
        try:
            print("Printing data: ")
            #tweet = data.split(',"text":')[1]
            #tweet = tweet.split(',"source"')[0]
            #print("Tweet variable assigned.")
            #print (data)
            """listener.i=listener.i+1
            print("I:",listener.i)
            if listener.i%10==0:
                listener.j=listener.j+1
            saveFile = open('test'+str(listener.j)+'.json','a')
            """
            """if listener.i==1:
                saveFile.write("[")
            if listener.i==500:
                saveFile.write(data+"]")
            else:
                saveFile.write(data+",")
            saveFile.close()"""
            saveFile = open('myTextFile.json','a')
            saveFile.write(data)
            saveFile.close()
            #if listener.i==50:
            #    exit()
            #print(data)
            #saveFile = open('myTweetsFile3.csv','r')
            #myReader = csv.reader(saveFile)
            #for r in myReader:
            #    j=0
            #    outFile = open('tweetsOnly.txt','a')
            #    for i in r:
            #        j=j+1;    
            #        if(j==4):
            #            print(i);
            #            outFile.write(i)
            #            outFile.write('\n')
            #outFile.close()
            return True
        
        except BaseException:
            print("Exception occured.")
            print(BaseException.__context__());
            time.sleep(5)
    
    def on_error(self, status):
        print("Printing status: ")
        print (status)
        return True

print("Starting program") 
auth = OAuthHandler(ckey, csecret)
print("OAuthHandler object returned and assigned.")
auth.set_access_token(atoken, asecret)
print("Access tokens set")
twitterStream = Stream(auth, listener())
print("Stream object created")
twitterStream.filter(track=["terrorist,firing,shooting,bomb,killed,terror attack,injured"],languages=["en"])
