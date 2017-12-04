import nltk
import pymongo
import mapping as mapping
import reverse_geocoder as rg

from pymongo import MongoClient
from bson.code import Code
from bson.json_util import dumps
from bson.son import SON
from geopy.geocoders import Nominatim
from nltk import ne_chunk
from nltk.chunk import conlltags2tree
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

def getLocations(tweets):
    countries = {}
    places = []
    for tweet in tweets:
        tweet['text'].title()
        tagged_tweet = nltk.pos_tag(word_tokenize(tweet))
        iob_tagged = tree2conlltags(nltk.chunk.ne_chunk(tagged_tweet))
        for word in iob_tagged:
            if 'GPE' in word[2]:
                places.append(word[0])

    geolocator = Nominatim()
    for place in places:
        location = geolocator.geocode(place)
        coordinates = (location.latitude, location.longitude)
        translation = rg.search(coordinates, mode=1)
        country = g[0]['cc']
        if not country in countries:
            countries[country] = 1
        else:
            countries[country] += 1
    return countries

def access(hashtags, keyword):
    print('Connecting...')
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['bdam']
    print('Connected')

    results = []
    unfilteredhashtagsize = 0
    for hashtag in hashtags:
        collection = db['twitter_{0}'.format(hashtag)]
        query = list(collection.find({"text": {"$regex": " " + keyword + " ", "$options": "i" } }, {'text':1,'_id':0} ))
        unfilteredhashtagsize += len(query)
        results.extend(query)

    #output = getLocations(results)

    # Extract all proper nouns from tweets under given hastag(s)
    #propernouns = findProperNouns(results)

    # Show frequency distribution for hashtag(s)
    #hashtagFreq = freqDist(propernouns, hashtags)

    return output



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
