import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from Tweet import Tweet
from SentimentAnalyser import SentimentAnalyser
from config import *



es = Elasticsearch()

class StreamCollector(StreamListener):

    def __init__(self):
        print("stream called")
 
        self.tweet_count=0

    def on_data(self, data):
        if self.tweet_count<7:
            print("on_data called")
            dict_data = json.loads(data)
            tweett = Tweet(dict_data["user"]["screen_name"],dict_data["created_at"],dict_data["text"])
            SA = SentimentAnalyser()
            stat = SA.findSentiment(tweett)
            if (stat):
                print("inserted tweet")
                self.tweet_count=self.tweet_count+1
                print(self.tweet_count)
                            
            else:
                print("failed to insert tweet")
            return True
        else:
            return False
        
            
        
            
        
    
    
                
        

    def on_failure(self, status):
        print (status)
                

    