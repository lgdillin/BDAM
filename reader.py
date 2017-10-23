import pprint, json
import pymongo
from pymongo import MongoClient
from bson.code import Code

def query():
    render_template('querypage.html', data=topFive())



def topFive(hashtag):
    # Create a connection
    client = MongoClient('mongodb://admin:Big.Data-1@ds147034.mlab.com:47034/tweets')
    db = client['tweets']
    #collection = db['twitter_{0}'.format(hashtag)]
    collection = db['twitter_BREAKING']
    collectionName = 'twitter_{0}'.format(hashtag)

    # Execute the map and reduce JavaScript files
    map = Code(open('map.js', 'r').read())
    reduce = Code(open('reduce.js', 'r').read())
    result = db['twitter_{0}'.format(hashtag)].map_reduce(map, reduce, "result")

    # Sort the query and map it into a dictionary
    sortedresult = result.find().sort([('value.count', -1)])
    data = {}
    for sr in sortedresult:
        data.update({sr['_id']:sr['value']['count']})

    return data
