import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch


from config import *



es = Elasticsearch()

class Database():
    def __init__(self):
        self.status = False

    def store(self, tweet):
        es.index(index="sentimentanalysis",
        doc_type="test-type",
        body={"author": tweet.author,
        "date": tweet.date,
        "message": tweet.message,
        "polarity": tweet.polarity,
        "subjectivity" : tweet.subjectivity,
        "sentiment": tweet.sentiment})
        self.status = True
        return self.status
		