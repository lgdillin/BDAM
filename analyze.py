import nltk
import pymongo

from pymongo import MongoClient

def access(hashtags):
    print('Connecting...')
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['bdam']
    print('Connected')

    
