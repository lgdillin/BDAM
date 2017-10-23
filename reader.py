import pprint, json
import pymongo
from pprint import pprint

from pymongo import MongoClient
from bson.code import Code
from bson.son import SON


def topFive(hashtag):
    # Create a connection
    client = MongoClient('mongodb://admin:Big.Data-1@ds147034.mlab.com:47034/tweets')
    #client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['tweets']
    collection = db['twitter_news']
    cursor = collection.find({})
    resultstring = ""
    for doc in cursor:
        resultstring = resultstring + doc
    return resultstring
    #collection = db['twitter_{0}'.format(hashtag)]
    #collectionName = 'twitter_{0}'.format(hashtag)
    #pipeline = [{"$unwind": "$tags"}, {"group": {"_id": "$tags", "count": {"$sum": 1}}}, {"$sort": SON([("count", -1), ("_id", -1)])}]
    #print(list(db.twitter_news.aggregate(pipeline)))
    #result = list(collection.aggregate(pipeline))
    #result = collection.count()
    #pprint.pprint(list(db.things.aggregate(pipeline)))
    # Execute the map and reduce JavaScript files
    #map = Code(open('map.js', 'r').read())
    #reduce = Code(open('reduce.js', 'r').read())
    #map = Code("function map() {var user = this.user.name.match(/\w+/g);if(user == null) {return;}for(var i = 0; i < user.length; ++i) {emit(this.user[i], {count:1});}}")
    #reduce = Code("function reduce(key, values) {var total = 0;for(var i = 0; i < values.length; ++i) {total += values[i].count;}return {count: total};}")
    #result = collection.map_reduce(map, reduce, collectionName)

    # Sort the query and map it into a dictionary
    #sortedresult = result.find().sort([('value.count', -1)])
    #data = {}
    #for sr in sortedresult:
        #data.update({sr['_id']:sr['value']['count']})

    #return data
