import nltk, random
from nltk.corpus import names

def gender_features(word):
    result = {'last_letter': word[-1]}
    #print(result)
    return result

names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)

featuresets = [(gender_features(n), g) for (n,g) in names]
print(featuresets)
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(classifier.classify(gender_features('Neo')))

print(nltk.classify.accuracy(classifier, test_set))
