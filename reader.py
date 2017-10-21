import pprint, json
import pymongo
from pymongo import MongoClient
from bson.code import Code


def topFive():
    client = MongoClient('mongodb://admin:Big.Data-1@ds147034.mlab.com:47034/tweets')
    db = client['tweets']
    collection = db['twitter_sport']

    map = Code(open('map.js', 'r').read())
    reduce = Code(open('reduce.js', 'r').read())
    result = db.twitter_sport.map_reduce(map, reduce, """{out: {inline:1}}""")
    resultstring = ""
    #for doc in result.find().sort( { total: -1 } ):
    #for doc in result.find():
    #sorted = result.find().sort('value', pymongo.DESCENDING)
    for doc in result.find():
        resultstring = resultstring + pprint.pformat(doc);

    return resultstring

# Query the server
def queryy():
    client = MongoClient('mongodb://lgdillin:Big.Data-1@bdam-shard-00-00-awflg.mongodb.net:27017,bdam-shard-00-01-awflg.mongodb.net:27017,bdam-shard-00-02-awflg.mongodb.net:27017/test?ssl=true&replicaSet=bdam-shard-0&authSource=admin', 27017)
    db = client['MONGODB']
    collection = db['MONGODB']

    result = ""
    for post in collection.find():
        result = result + pprint.pformat(post)

    return result
    #print(json.loads(result)["content"])
    #return food["content"]
    #return pprint.pformat(collection.count())
    #return pprint.pformat(collection.find())
    #for post in collection.find():

    #pprint.pprint(collection.find_one())
    #return pprint.pformat(collection.find_one())
    #return pprint.pformat(db.collection_names())

def test():
    return "works"
