#import cPickle as pickle
import _pickle as pickle
import numpy as np

from nltk.corpus import twitter_samples
from textblob.classifiers import NaiveBayesClassifier



f = open('testing-classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()




#Turn tweets datasets into lists of tuples
negative_tweets = twitter_samples.strings('negative_tweets.json')
negative_tweets = [(value, 'negative') for value in negative_tweets]

positive_tweets = twitter_samples.strings('positive_tweets.json')
positive_tweets = [(value, 'positive') for value in positive_tweets]
#
# # Split into training and test data
# ntweets_training = negative_tweets[:int(len(negative_tweets)*0.275)]
ntweets_test = negative_tweets[int(len(negative_tweets)*0.025):]
#
# ptweets_training = positive_tweets[:int(len(positive_tweets)*0.275)]
ptweets_test = positive_tweets[int(len(positive_tweets)*0.025):]
#
# training_tweets = np.array(ptweets_training + ntweets_training)
test_tweets = ptweets_test + ntweets_test
#
# # Train the classifier
# classifier = NaiveBayesClassifier(training_tweets)
#
# # Test it outb
# test = "Trump's foreign policy is not favorable to America."
# #print(classifier.classify(test))
#
# print("Classifier accuracy: ", classifier.accuracy(test_tweets))

# https://stackoverflow.com/questions/15150339/python-memory-error-sklearn-huge-input-data

# f = open('testing-classifier.pickle', 'wb')
# pickle.dump(classifier, f)
# f.close()

#print("Classifier accuracy: ", classifier.accuracy(test_tweets))
prob_dist = classifier.prob_classify("Trump's arrogance is damaging America's global reputation.")
print("classifying: ", "'Trump's arrogance is damaging America's global reputation.'")
print("chance of labeling positive: ", round(prob_dist.prob("positive"), 2))
print("Chance of labeling negative: ", round(prob_dist.prob("negative"), 2))


# Save the trained classifier
# p = pickle.Pickler(open('simplebayes_classifier.pickle', 'wb'))
# p.fast = True
# pickle.dump(classifier, p)
# p.close()
