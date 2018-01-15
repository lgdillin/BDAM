import pprint, json
import pymongo

from pymongo import MongoClient
from bson.code import Code
from bson.son import SON
from bson.json_util import dumps


# under construction?
def mostActiveTweeters(hashtag):

    # Create a connection
    print("Connecting..")
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    print("Connected.")

    # Access database
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]
    pipeline = [ {"$unwind": "$user.screen_name"}, {"$group": {"_id": "$user.screen_name", "count": {"$sum": 1}}}, {"$sort": SON([("count", -1), ("_id", -1)])} ]
    jsonOut = json.loads(json.dumps(list(collection.aggregate(pipeline))))
    data = {}
    for doc in jsonOut:
        data.update({doc['_id']:doc['count']})
    return data
    #return json.dumps(list(collection.aggregate(pipeline)), ensure_ascii=True).encode('utf8')

def getUserTweets(hashtag, screen_name):
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]
    results = list(collection.find( {'user.screen_name': screen_name}, {'text':1, 'user.screen_name':1, '_id':0} ))

    return results

# This function is for debugging purposes.
# It simply outputs the entire given collection as a JSON string
def rawResponse(hashtag):
    # Create a connection
    print("Connecting..")
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    print("Connected.")

    # Access database
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]
    return dumps(list(collection.find()))

def tweetsDash():
    # Create a Connection
    print("Connecting...")
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    print("Connected")

    db = client['bdam']
    colls = db.collection_names()

    colls.remove('system.indexes') # This is an Mlab specific command

    return colls
