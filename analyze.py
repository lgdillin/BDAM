import nltk
import pymongo
import mapping as mapping
import reverse_geocoder as rg
import pickle
import operator

from collections import defaultdict, Counter
from geotext import GeoText
from pymongo import MongoClient
from bson.code import Code
from bson.json_util import dumps
from bson.son import SON
from geopy.geocoders import Nominatim
from nltk.tokenize import word_tokenize, TweetTokenizer

f = open('naive-bayes-twitter.pickle', 'rb')
classifier = pickle.load(f)
f.close()

# this is necessary for the classifier to break down sentences
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

def BuildDataset(locations):

    # Load the classifier
    data = []
    geolocator = Nominatim(timeout=30)
    for location in locations:

        # classify the given tweet
        text = location['text']
        sent = classifier.classify(format_sentence(text))

        location = location['user']['location'].title()
        location = geolocator.geocode(location)

        # If the location is garbage throw it out of the results
        if location is None:
            continue

        coordinates = (location.latitude, location.longitude)
        translation = rg.search(coordinates, mode=1)
        country = translation[0]['cc'].lower()

        datapoint = (country, sent)
        data.append(datapoint)
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
    d2 = defaultdict(float)
    d1 = defaultdict(float)

    # Build the numerator
    for country in dataset:
        if country[1] == 'positive':
            d2[country[0]] += 1
        else:
            d2[country[0]] = 0

    # Build the denominator
    for country in dataset:
        d1[country[0]] += 1

    print(d2)
    print(d1)
    final = {k: d2[k]/d1[k] for k in d1.keys() & d2}
    #return mapping.drawmap(keyword,final)
    return (final, d1)
