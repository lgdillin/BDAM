import pprint, json
import pymongo
from pymongo import MongoClient
from bson.code import Code

def query():
    render_template('querypage.html', data=topFive())



def topFive(hashtag):
    # Create a connection
    #client = MongoClient('mongodb://admin:Big.Data-1@ds147034.mlab.com:47034/tweets')
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]
    print(collection)

    # Execute the map and reduce JavaScript files
    #map = Code(open('map.js', 'r').read())
    #reduce = Code(open('reduce.js', 'r').read())
    map = Code("function map() {var user = this.user.name.match(/\w+/g);if(user == null) {return;}for(var i = 0; i < user.length; ++i) {emit(this.user[i], {count:1});}}")
    reduce = Code("function reduce(key, values) {var total = 0;for(var i = 0; i < values.length; ++i) {total += values[i].count;}return {count: total};}")
    result = collection.map_reduce(map, reduce, "result")

    # Sort the query and map it into a dictionary
    sortedresult = result.find().sort([('value.count', -1)])
    data = {}
    for sr in sortedresult:
        data.update({sr['_id']:sr['value']['count']})

    return data
