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

def extract_features(document, word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def classifyString(string, classifier, word_features):
    classifier = classifier
    word_features = word_features
    result = classifier.classify(extract_features(string.split(), word_features))
    return result



def getTweetFeatures():
    # Give a dataset of tweets its respective sentiment
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    negative_tweets = [(value, 'negative') for value in negative_tweets]

    positive_tweets = twitter_samples.strings('positive_tweets.json')
    positive_tweets = [(value, 'positive') for value in positive_tweets]

    # Clean the lists and concatenate them
    ntweets = []
    ptweets = []
    for (words, sentiment) in negative_tweets:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        ntweets.append((words_filtered, sentiment))

    for (words, sentiment) in positive_tweets:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        ptweets.append((words_filtered, sentiment))

    # split the datasets into training and test sets
    # the split is (training, test) -> (80, 20)
    ntweets_training = ntweets[:int(len(ntweets)*0.8)]
    ntweets_test = ntweets[int(len(ntweets)*0.8):]

    ptweets_training = ptweets[:int(len(ptweets)*0.8)]
    ptweets_test = ptweets[int(len(ptweets)*0.8):]

    training_tweets = ptweets_training + ntweets_training
    test_tweets = ptweets_test + ntweets_test

    # Build our training set
    #training_set = nltk.classify.apply_features(extract_features, training_tweets)

    # train the classifier
    #classifier = nltk.classify.NaiveBayesClassifier.train(training_set)

    #classifier.show_most_informative_features(15)
    return training_tweets

#f = open('twitter_sentiment_analysis_tested.pickle', 'wb')
#pickle.dump(classifier, f)
#f.close()

#print(test_tweets, encoding='utf-8')
#print(nltk.classify.accuracy(classifier, test_tweets) * 100)



# f = open('my_classifier.pickle', 'rb')
# classifier = pickle.load(f)
# f.close()
