
import json

from elasticsearch import Elasticsearch
from elasticsearch_dsl import search
es = Elasticsearch()


class DataTable:
        def __init__(self):
                pass
                
        def displayDataTable(self):

                doc =   {'size' : 5,'query': {'match_all' : {} } }

                res = es.search( index="sentimentanalysis", body=doc)
                
                results = []
                
                

                
                count=0
                for hit in res['hits']['hits']:
                    tweet = hit['_source']['message']
                    char_list = [tweet[j] for j in range(len(tweet)) if ord(tweet[j]) in range(65536)]
                    if(len(char_list)<75):
                        length = len(char_list)
                    else:
                        length = 75
                    chars = [char_list[j] for j in range(length)] 
                    tweet=''
                    for j in chars:
                        tweet=tweet+j    
                    results.append([hit['_source']['author'],tweet])
                    
                    count+=1

                
                return results


                
