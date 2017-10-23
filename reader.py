import pprint, json
import pymongo

from pymongo import MongoClient
from bson.code import Code
from bson.son import SON
from bson.json_util import dumps

def rawResponse(hashtag):
    # Create a connection
    print("Connecting..")
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    print("Connected.")

    # Access database
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]
    return dumps(list(collection.find()))


def topFive(hashtag):

    # Create a connection
    print("Connecting..")
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    print("Connected.")

    # Access database
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]

    query = collection.find()
    l = list(doc)
    type(doc)
    type(l)
    #db.command('aggregate', 'twitter_sport', pipeline=pipeline, explain=True)
    #return
    #result = list(collection.aggregate(pipeline))
    #result = collection.count()
    #pprint.pprint(list(db.things.aggregate(pipeline)))
    # Execute the map and reduce JavaScript files
    #map = Code(open('map.js', 'r').read())
    #reduce = Code(open('reduce.js', 'r').read())
    #map = Code("function map() {var user = this.user.name.match(/\w+/g);if(user == null) {return;}for(var i = 0; i < user.length; ++i) {emit(this.user[i], {count:1});}}")
    #reduce = Code("function reduce(key, values) {var total = 0;for(var i = 0; i < values.length; ++i) {total += values[i].count;}return {count: total};}")
    #result = collection.map_reduce(map, reduce, "twitter_sport")

    # Sort the query and map it into a dictionary
    #sortedresult = result.find().sort([('value.count', -1)])
    #sortedresult = collection.aggregate(pipeline)
    data = json.loads(dumps(l))
    #for sr in cursor:
    #    print(sr)
        #data.update({sr['_id']:sr['value']['count']})
    print(data)
    return data

    #return data

    #pipeline = [{"$unwind": "$tags"}, {"$group": {"_id": "$tags", "count": {"$sum": 1}}}, {"$sort": SON([("count", -1), ("_id", -1)])}]
    #client = MongoClient('mongodb://lgdillin:Big.Data-1@bdam-shard-00-00-awflg.mongodb.net:27017,bdam-shard-00-01-awflg.mongodb.net:27017,bdam-shard-00-02-awflg.mongodb.net:27017/test?ssl=true&replicaSet=bdam-shard-0&authSource=admin', 27017)
    #client = MongoClient('ds147034.mlab.com/tweets', 29435)
