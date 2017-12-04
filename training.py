import nltk
import pickle

from nltk.tag import pos_tag, pos_tag_sents
from nltk.corpus import twitter_samples



def get_words_in_tweets(tweets):
    all_words = []
    for(words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features



# Give a dataset of tweets its respective sentiment
negative_tweets = twitter_samples.strings('negative_tweets.json')
negative_tweets = [(value, 'negative') for value in negative_tweets]

positive_tweets = twitter_samples.strings('positive_tweets.json')
positive_tweets = [(value, 'positive') for value in positive_tweets]

# stick the two lists together and clean them
tweets = []
for (words, sentiment) in negative_tweets + positive_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

word_features = get_word_features(get_words_in_tweets(tweets))

# Build our training set
training_set = nltk.classify.apply_features(extract_features, tweets)

# train the classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

test = "Trump's foreign policy is damaging America's reputation globally."

print(classifier.classify(extract_features(test.split())))

f = open('twitter_sentiment_analysis.pickle', 'wb')
pickle.dump(classifier, f)
f.close()

# f = open('my_classifier.pickle', 'rb')
# classifier = pickle.load(f)
# f.close()
