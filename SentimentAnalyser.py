

from textblob import TextBlob
from elasticsearch import Elasticsearch
from Database import Database
from Tweet import Tweet

class SentimentAnalyser():


    def findSentiment(self,tweet):
        print ("findSentiment works")
        

        tweet_content = TextBlob(tweet.message)  
        sentiment_value = self.calculatePolarity(tweet_content)        
        tweet.set_polarity(tweet_content.sentiment.polarity,  tweet_content.sentiment.subjectivity, sentiment_value)
        dt = Database() 
        st=dt.store(tweet)
        return st


    def calculatePolarity(self,tweetc):
        polarity_value = tweetc.sentiment.polarity
        if polarity_value <0:
            sentiment = "negative"
        elif polarity_value==0:
            sentiment = "neutral"
        else:
            sentiment = "positive"
        return sentiment
           		
""" tt = Tweet("author", "date", "bad")
SA=SentimentAnalyser()	
SA.findSentiment(tt) """