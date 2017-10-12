import pprint, json
from pymongo import MongoClient

def populate():
    client = MongoClient('mongodb://lgdillin:Big.Data-1@bdam-shard-00-00-awflg.mongodb.net:27017,bdam-shard-00-01-awflg.mongodb.net:27017,bdam-shard-00-02-awflg.mongodb.net:27017/test?ssl=true&replicaSet=bdam-shard-0&authSource=admin', 27017)
    db = client['MONGODB']
    collection = db['MONGODB']

    #Populate with some values
    post = {"content":"One day I woke up and took a shit and then went to walmart. I saw a giant bread toaster"}
    post_id = collection.insert(post)
    post = {"content":"Yesterday on the news a brown person are abused by the police"}
    post_id = collection.insert(post)
    post = {"content":"Words in a string are useful sometimes, the context is irrelevant"}
    return

# Query the server
def query():
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
