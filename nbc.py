# This code is here to show editors how the classifier was built
# its also here in case I want to do any more work in the future

import nltk
import pickle
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import twitter_samples

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})


negative_tweets = twitter_samples.strings('negative_tweets.json')
negative_tweets = [(format_sentence(value), 'negative') for value in negative_tweets]

positive_tweets = twitter_samples.strings('positive_tweets.json')
positive_tweets = [(format_sentence(value), 'positive') for value in positive_tweets]

training = (positive_tweets[:int((.8)*len(positive_tweets))]
        + negative_tweets[:int((.8)*len(negative_tweets))])
test = (positive_tweets[int((.8)*len(positive_tweets)):]
        + negative_tweets[int((.8)*len(negative_tweets)):])



classifier = NaiveBayesClassifier.train(training)
classifier.show_most_informative_features()

# f = open('naive-bayes-twitter.pickle', 'wb')
# pickle.dump(classifier, f)
# f.close()
