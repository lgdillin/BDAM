import nltk
import pymongo

import mapping as mapping

from pymongo import MongoClient
from bson.code import Code
from bson.son import SON
from bson.json_util import dumps
from nltk.tag import pos_tag, pos_tag_sents
from geotext import GeoText

# Returns all proper nouns from the set of tweets
def findProperNouns(tweets):
    nountuples = []
    for tweet in tweets:
        nountuples.extend(pos_tag(tweet['text'].split()))

    propernouns = [word for word,pos in nountuples if pos == 'NNP']
    return propernouns

def freqDist(propernouns, hashtags):
    cfd = nltk.ConditionalFreqDist( (hashtag, pnoun)
        for hashtag in hashtags
        for pnoun in propernouns)
    #return cfd.tabulate(conditions=hashtags, samples=propernouns)

def getLocations(tweets):

    words = []
    for tweet in tweets:
        words.append(tweet['text'].title())
    words = ' '.join(words)
    places = GeoText(str(words)).country_mentions
    return places
    # words = []
    # citiesAndCountries = []
    # for tweet in tweets:
    #     words.extend(tweet['text'].title().split())
    #
    # for word in words:
    #     i = GeoText(word)

def access(hashtags, filter):
    print('Connecting...')
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['bdam']
    print('Connected')

    results = []
    unfilteredhashtagsize = 0
    for hashtag in hashtags:
        collection = db['twitter_{0}'.format(hashtag)]
        query = list(collection.find({"text":
            {"$regex": " " + filter + " ", "$options": "i" } }, {'text':1,'_id':0} ))
        unfilteredhashtagsize += len(query)
        results.extend(query)

    output = getLocations(results)

    # Extract all proper nouns from tweets under given hastag(s)
    #propernouns = findProperNouns(results)

    # Show frequency distribution for hashtag(s)
    #hashtagFreq = freqDist(propernouns, hashtags)

    return results
