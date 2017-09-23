import time
import datetime
from pymongo import MongoClient
import json
import tweepy
from tweepy import OAuthHandler
#############
#   PyMongo can be installed with pip: pip install pymongo
#   Tweepy can be installed wit pip: pip install tweepy
#############

#Just for now
import os

# I really hate that our keys are public when hosted on github :( not secure
consumer_key = 'vpvdYQoEvBKYoqXz4SWX8l9PZ'
consumer_secret = 'LKi0n0ZlyU4fTElfp8CBOOw89YFhEyl7P9tRB2DrILTVWsKDo5'
access_token = '910189018905825285-W0P6aue3kstAqK3RoEFJAGIWYvtpIOZ'
access_token_secret = 'Fljltt5C7deqlr91kkzA6WwO14KZlyqFgG0AHoum6Oy0L'

#
auth = OAuthHandler(consumer_key, consumer_secret)

#
auth.set_access_token(access_token, access_token_secret)

#
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

# If API fails
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
# mongodb://heroku_n2tfcpfx:d09ttqk88oe9r5ag0v2okkj0bs@dbh30.mlab.com:27307/heroku_n2tfcpfx
# client = MongoClient('mongodb://heroku_n2tfcpfx:d09ttqk88oe9r5ag0v2okkj0bs@dbh30.mlab.com:27307/heroku_n2tfcpfx', 27307)
# client = open(os.path.dirname(os.path.realpath("test.txt")), "r")
# print(client.read())
client = MongoClient('localhost', 27017)

client = MongoClient()
db = client['MONGODB']

start_time = time.time()
last_sun = str(datetime.date.today() -
               datetime.timedelta(days=datetime.date.today().weekday() + 1))
last_mon = str(datetime.date.today() -
               datetime.timedelta(days=datetime.date.today().weekday() + 7))
searchQuery = ['#news', '#sport', '#BREAKING']


def crawler(searchQuery, maxTweets=100000, tweetsPerQry=100):
    for word in searchQuery:
        max_id = -1# LS
        tweetCount = 0
        collection = db['twitter_{0}'.format(word[1:])]
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    new_tweets = api.search(lang="en",
                                            q=word, count=tweetsPerQry, since=last_mon, until=last_sun)
                else:
                    new_tweets = api.search(lang="en",
                                            q=word, count=tweetsPerQry, since=last_mon, until=last_sun, max_id=str(max_id - 1))

                if not new_tweets:
                    print("No more tweets found")
                    break

                for tweet in new_tweets:
                    # print(tweet)
                    collection.insert(json.loads(json.dumps(tweet._json)))

                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break

crawler(searchQuery=searchQuery)
