import nltk
import pickle
import random

from nltk.tag import pos_tag, pos_tag_sents
from nltk.tokenize import word_tokenize
from nltk.corpus import twitter_samples

def get_features(tweet):
    return {word.lower(): (word in word_tokenize(tweet.lower())) for word in training_tokens}

# Give a dataset of tweets its respective sentiment
negative_tweets = twitter_samples.strings('negative_tweets.json')
negative_tweets = [(value, 'negative') for value in negative_tweets]

positive_tweets = twitter_samples.strings('positive_tweets.json')
positive_tweets = [(value, 'positive') for value in positive_tweets]

# Clean the lists and concatenate them
# ntweets = []
# ptweets = []
# for (words, sentiment) in negative_tweets:
#     words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
#     ntweets.append((words_filtered, sentiment))
#
# for (words, sentiment) in positive_tweets:
#     words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
#     ptweets.append((words_filtered, sentiment))

# split the datasets into training and test sets
# the split is (training, test) -> (80, 20)
ntweets_training = negative_tweets[:int(len(negative_tweets)*0.001)]
ntweets_test = negative_tweets[int(len(negative_tweets)*0.1):]

ptweets_training = positive_tweets[:int(len(positive_tweets)*0.001)]
ptweets_test = positive_tweets[int(len(positive_tweets)*0.1):]

training_tweets = ptweets_training + ntweets_training
test_tweets = ptweets_test + ntweets_test
print(training_tweets[0])

# Extract features
training_tokens = set(word.lower() for passage in training_tweets for word in word_tokenize(passage[0]))
training_features = [({word: (word in word_tokenize(x[0])) for word in training_tokens}, x[1]) for x in training_tweets]

test_tokens = set(word.lower() for passage in test_tweets for word in word_tokenize(passage[0]))
test_features = [({word: (word in word_tokenize(x[0])) for word in test_tokens}, x[1]) for x in test_tweets]

classifier = nltk.NaiveBayesClassifier.train(training_features)

print(nltk.classify.accuracy(classifier, test_features))

testword = "trump is ruining america's global reputation"
print(classifier.classify(get_features(testword)))
#
# f = open('bayes_classifier', 'wb')
# pickle.dump(classifier, f)
# f.close()
