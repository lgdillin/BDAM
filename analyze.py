import nltk
import pymongo

from pymongo import MongoClient

from bson.code import Code
from bson.son import SON
from bson.json_util import dumps

from nltk.tag import pos_tag
NLTK_DATA = './tagger/'
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import LabelEncoder
# from sklearn.linear_model import SGDClassifier
# from sklearn.metrics import classification_report as clsr
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cross_validation import train_test_split as tts

def findProperNouns(tweets):
    nountuples = []
    for tweet in tweets:
        print(tweet)
        nountuples.extend(pos_tag(tweet['text'].split()))

    propernouns = [word for word,pos in nountuples if pos == 'NNP']
    return propernouns

def access(hashtags):
    print('Connecting...')
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    db = client['bdam']
    print('Connected')

    results = []
    for hashtag in hashtags:
        print(hashtag)
        collection = db['twitter_{0}'.format(hashtag)]
        results.extend(list(collection.find({}, {'text':1,'_id':0} )))

    propernouns = findProperNouns(results)

    return propernouns



# @timeit
# def build_and_evaluate(X, y,
#     classifier=SGDClassifier, outpath=None, verbose=True):
#
#     @timeit
#     def build(classifier, X, y=None):
#         """
#         Inner build function that builds a single model.
#         """
#         if isinstance(classifier, type):
#             classifier = classifier()
#
#         model = Pipeline([
#             ('preprocessor', NLTKPreprocessor()),
#             ('vectorizer', TfidfVectorizer(
#                 tokenizer=identity, preprocessor=None, lowercase=False
#             )),
#             ('classifier', classifier),
#         ])
#
#         model.fit(X, y)
#         return model
#
#     # Label encode the targets
#     labels = LabelEncoder()
#     y = labels.fit_transform(y)
#
#     # Begin evaluation
#     if verbose: print("Building for evaluation")
#     X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2)
#     model, secs = build(classifier, X_train, y_train)
#
#     if verbose:
#         print("Evaluation model fit in {:0.3f} seconds".format(secs))
#         print("Classification Report:\n")
#
#     y_pred = model.predict(X_test)
#     print(clsr(y_test, y_pred, target_names=labels.classes_))
#
#     if verbose:
#         print("Building complete model and saving ...")
#     model, secs = build(classifier, X, y)
#     model.labels_ = labels
#
#     if verbose:
#         print("Complete model fit in {:0.3f} seconds".format(secs))
#
#     if outpath:
#         with open(outpath, 'wb') as f:
#             pickle.dump(model, f)
#
#         print("Model written out to {}".format(outpath))
#
#     return model
