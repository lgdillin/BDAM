#import cPickle as pickle
import _pickle as pickle
import numpy as np

from nltk.corpus import twitter_samples
from textblob.classifiers import NaiveBayesClassifier

# Turn tweets datasets into lists of tuples
negative_tweets = twitter_samples.strings('negative_tweets.json')
negative_tweets = [(value, 'negative') for value in negative_tweets]

positive_tweets = twitter_samples.strings('positive_tweets.json')
positive_tweets = [(value, 'positive') for value in positive_tweets]

# Split into training and test data
ntweets_training = negative_tweets[:int(len(negative_tweets)*0.25)]
ntweets_test = negative_tweets[int(len(negative_tweets)*0.2):]

ptweets_training = positive_tweets[:int(len(positive_tweets)*0.25)]
ptweets_test = positive_tweets[int(len(positive_tweets)*0.15):]

training_tweets = np.array(ptweets_training + ntweets_training)
#test_tweets = ptweets_test + ntweets_test

# Train the classifier
classifier = NaiveBayesClassifier(training_tweets)

# Test it out
test = "Trump's foreign policy is not favorable to America."
print(classifier.classify(test))

#print(classifier.accuracy(test_tweets))
# https://stackoverflow.com/questions/15150339/python-memory-error-sklearn-huge-input-data


# Save the trained classifier
# p = pickle.Pickler(open('bayes_classifier.pickle', 'wb'))
# p.fast = True
# pickle.dump(classifier, p)
# p.close()
with open('bayes-classifier.pickle', 'wb') as pickle_file:
    pickle.dump(classifier, pickle_file)
