import geocoder
# http://geocoder.readthedocs.io/providers/Google.html#geocoding
g = geocoder.google("LA")
print(g)

# import nltk
# import os
# from nltk.tag.stanford import StanfordNERTagger
# from nltk.tokenize import word_tokenize
#
# #java_path = "C:\Program Files\Java\jre1.8.0_131\\bin"
# #config_java("C:\Program Files\Java\jre1.8.0_131\\bin")
# # [xx] add classpath option to config_java?
#
# nltk.internals.config_java("C:\Program Files\Java\jre1.8.0_131\\bin\java.exe")
#
# # Change the path according to your system
# stanford_classifier = 'C:\\NER\\stanford-ner-2015-12-09\\classifiers\\english.all.3class.distsim.crf.ser.gz'
# stanford_ner_path = 'C:\\NER\\stanford-ner-2015-12-09\\stanford-ner.jar'
#
# # Creating Tagger Object
# st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')
#
# text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
#
# tokenized_text = word_tokenize(text)
# classified_text = st.tag(tokenized_text)
#
# print(classified_text)




# import requests
# from extraction import Extractor
# url = 'http://wikipedia.org'
# html = requests.get('http://url').text
# extracted = Extractor().extract(html)
# canonical_url = extracted.url if extract.url else url
#
#
# # You can now access all of the places found by the Extractor
# print (e.places)







import places
pc = places.Place(['Cleveland', 'Ohio', 'United States'])

pc.set_countries()
print (pc.countries) #['United States']

pc.set_regions()
print (pc.regions) #['Ohio']

pc.set_cities()
print (pc.cities) #['Cleveland']

print (pc.address_strings) #['Cleveland, Ohio, United States']
