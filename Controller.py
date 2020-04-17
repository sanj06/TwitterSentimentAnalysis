
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from StreamCollector import StreamCollector
from Display import Display
import time

from config import *



class Controller():

    def __init__(self):
        self.status = False

    def search(self,key,location):
        print("search called")
        print(key)
        listener = StreamCollector()
        auth = OAuthHandler(consumer_key,consumer_secret)
	
        
        auth.set_access_token(access_token,access_token_secret)

        stream = Stream(auth, listener)

        stream.filter(track=[key],languages=['en'])
        stream.filter(profile_country=[location])
        #time.sleep(3)
        #stream.disconnect()
        print("Filtered")
        self.status = True
        return self.status

        

    def display(self):
        d = Display()
        result = d.displayResult()
        return result









    

