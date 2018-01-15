import nltk
import pickle

from nltk.tokenize import word_tokenize

def get_features(tweet):
    return {word.lower(): (word in word_tokenize(tweet.lower())) for word in training_tokens}

train = [('#I love @this 1234 sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('This is my best work.', 'pos'),
("What an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('He is my sworn enemy!', 'neg'),
('My boss is horrible.', 'neg')]

test = [('The beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg') ]

print(train[0])
training_tokens = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
training_tweets = [({word: (word in word_tokenize(x[0])) for word in training_tokens}, x[1]) for x in train]

test_tokens = set(word.lower() for passage in test for word in word_tokenize(passage[0]))
test_tweets = [({word: (word in word_tokenize(x[0])) for word in test_tokens}, x[1]) for x in test]

classifier = nltk.NaiveBayesClassifier.train(training_tweets)
#print(classifier.show_most_informative_features())
print(nltk.classify.accuracy(classifier, test_tweets))

testword = "trump is ruining america's global reputation"

print(classifier.classify(get_features(testword)))

# f = open('ex_c', 'wb')
# pickle.dump(classifier, f)
# f.close()
