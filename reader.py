from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://lgdillin:Big.Data-1@bdam-shard-00-00-awflg.mongodb.net:27017,bdam-shard-00-01-awflg.mongodb.net:27017,bdam-shard-00-02-awflg.mongodb.net:27017/test?ssl=true&replicaSet=bdam-shard-0&authSource=admin', 27017)
db = client['MONGODB']

post = {"author":"liam"}
collection = db.MONGODB
post_id = collection.insert_one(post).inserted_id
pprint.pprint(collection.find_one())
# document = client.db.collection.find_one({'author':'liam'})

'''
collection = db.MONGODB
for i in post:
    pprint.pprint(i)
'''
