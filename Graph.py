
import json

from elasticsearch import Elasticsearch
from elasticsearch_dsl import search
es = Elasticsearch()

class Graph:
    def __init__(self):
            pass


    def displayGraph(self):
            doc =   {'size' : 10000,'query': {'range' : {'polarity': { 'gte' : -1, 'lte' : 1} } } }

            res = es.search( index="tsa", body=doc)
                
            sum=0
            count=0
            for hit in res['hits']['hits']:
                sum+=hit['_source']['polarity']
                count+=1

            avg = sum/count
            return avg
