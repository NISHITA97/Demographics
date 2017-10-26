import pymongo
import json
from textblob import TextBlob
from pymongo import MongoClient
from twython import TwythonStreamer
from twython import Twython
import time
from httplib import IncompleteRead
from requests.exceptions import ChunkedEncodingError

consumer_key = '9PB9uI9KQblQP4BvyystztFeu'
consumer_secret = 'RinMb7l6HpDD0K1gVtGbSVnpQmGY3QzojPlWkMfXx67LnsXiRL'
access_token = '4656524534-Ycw1XeA7wevKNGZ7EkEvqvzDKw9giyigx6pBQ07'
access_token_secret = 'vdMeJq1zjGNs37YBolZZDuBz3RyR83vB2RVgecweAYIZ2'

connection=MongoClient()
db=connection['twitterdb1']

cnt=0
twitter = Twython(consumer_key, consumer_secret,
                         access_token, access_token_secret)
class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
    
        if 'text' in data:
            
            record={}
            global cnt
            global twitter
            time.sleep(0.5)
            if(cnt==75000):
                self.disconnect()
            print cnt,"\t"
            tweet_text= data['text'].encode('utf-8')
            analysis=TextBlob(data['text'])
            polarity=analysis.sentiment.polarity
            if(polarity!=0):
                cnt=(cnt)+1
                userid=data['user']['id_str']
                userdata=twitter.lookup_user(user_id=userid)
                for user in userdata:
                    record['tweet']= tweet_text
                    record['user_id']=userid
                    record['screen_name']=user['screen_name']
                    record['description']=user['description']
                    record['lang']=user['lang']
                    record["verified"]=user["verified"]
                    record['location']=user['location']
                    record["statuses_count"]=user["statuses_count"]
                    record["friends_count"]=user["friends_count"]   
                    record["followers_count"]=user["followers_count"]
                if(db['record_db2'].insert(record)):
                    print "insert success!"
                print record
            

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

streamer = TweetStreamer(consumer_key, consumer_secret,
                         access_token, access_token_secret)
while True:
    try:
        streamer.statuses.filter(track = "a",lang='en')
        
    except IncompleteRead:
        # Oh well, reconnect and keep trucking
        continue
    except ChunkedEncodingError:
        continue
    except KeyboardInterrupt:
        # Or however you want to exit this loop
        stream.disconnect()
        break
