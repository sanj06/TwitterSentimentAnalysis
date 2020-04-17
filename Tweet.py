import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch


from config import *



es = Elasticsearch()

class Tweet():
    def __init__(self, author, date, message, polarity=0, subjectivity=0, sentiment="neutral"):
        self.author = author
        self.date = date
        self.message = message
        self.polarity = polarity
        self.subjectivity = subjectivity
        self.sentiment = sentiment
        print (self.author, self.date, self.message, self.polarity, self.subjectivity, self.sentiment)
        print ("Tweet intialised")

    def set_polarity(self, polarity, subjectivity, sentiment):
        self.polarity = polarity
        self.subjectivity = subjectivity
        self.sentiment = sentiment
        print (self.author, self.date, self.message, self.polarity, self.subjectivity, self.sentiment)

 