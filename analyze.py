import nltk
import pymongo
import mapping as mapping
import reverse_geocoder as rg
import sentiment as sentiment
import pickle

from geotext import GeoText
from pymongo import MongoClient
from bson.code import Code
from bson.json_util import dumps
from bson.son import SON
from geopy.geocoders import Nominatim
from nltk import ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize, TweetTokenizer



def BuildDataset(locations):

    #countries = {}
    data = []
    geolocator = Nominatim()
    for location in locations:

        # Give the tweet a positive/negative label
        # extract_features(location['text'].split())
        text = location['text']
        sent = sentiment.classifyString(text)



        location = location['user']['location'].title()
        location = geolocator.geocode(location)

        # If the location is garbage...
        if location is None:
            continue

        coordinates = (location.latitude, location.longitude)
        translation = rg.search(coordinates, mode=1)
        country = translation[0]['cc']
        # if not country in countries:
        #     print(country)
        #     countries[country] = 1
        # else:
        #     countries[country] += 1

        datapoint = (country, sent)
        data.insert(datapoint)
    return data


def getTweets(hashtags, keyword):
    print('Connecting...')
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['bdam']
    print('Connected')


    query = {"user.location":{"$ne": ""},"text":{"$regex":"'+keyword+'","$options":"i"}}
    results = []
    unfilteredhashtagsize = 0
    for hashtag in hashtags:
        collection = db['twitter_{0}'.format(hashtag)]
        docs = list(collection.find({"user.location":{"$ne": ""},"text":{"$regex":keyword,"$options":"i"}}))

        unfilteredhashtagsize += len(docs)
        results.extend(docs)

    dataset = BuildDataset(results)
    dictionary = dict(dataset)
    print(dictionary)
    return locations




# def access(hashtags, keyword):
#     print('Connecting...')
#     client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
#     db = client['bdam']
#     print('Connected')
#
#     results = []
#     unfilteredhashtagsize = 0
#     for hashtag in hashtags:
#         collection = db['twitter_{0}'.format(hashtag)]
#         query = list(collection.find({"text": {"$regex": " " + keyword + " ", "$options": "i" } }, {'text':1,'_id':0} ))
#         unfilteredhashtagsize += len(query)
#         results.extend(query)
#     output = getLocations(results)
#     #output = "heey"
#     # Extract all proper nouns from tweets under given hastag(s)
#     #propernouns = findProperNouns(results)
#     # Show frequency distribution for hashtag(s)
#     #hashtagFreq = freqDist(propernouns, hashtags)
#     return

# # Returns all proper nouns from the set of tweets
# def findProperNouns(tweets):
#     nountuples = []
#     for tweet in tweets:
#         nountuples.extend(pos_tag(tweet['text'].split()))
#
#     propernouns = [word for word,pos in nountuples if pos == 'NNP']
#     return propernouns
#
# def freqDist(propernouns, hashtags):
#     cfd = nltk.ConditionalFreqDist( (hashtag, pnoun)
#         for hashtag in hashtags
#         for pnoun in propernouns)
#     #return cfd.tabulate(conditions=hashtags, samples=propernouns)
