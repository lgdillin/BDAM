# import geocoder
# # http://geocoder.readthedocs.io/providers/Google.html#geocoding
# g = geocoder.google('LA')
# print(g)

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.raw)

#print(g.geojson.country)

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk import ne_chunk
# from nltk.chunk import conlltags2tree, tree2conlltags
# sentence = word_tokenize("I want to go with John, from Delhi to Mumbai, to work at Google.")
# tagged = nltk.pos_tag(sentence)
# print(tagged)
# entities = nltk.chunk.ne_chunk(tagged)
# print(entities)
#
# iob_tagged = tree2conlltags(entities)
# print(iob_tagged)
#
# for word in iob_tagged:
#     if 'GPE' in word[2]:
#         g = geocoder.google(word[0])
#         print(g)
        #print (g.country)

#entities

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







# import places
# pc = places.Place(['Cleveland', 'Ohio', 'United States'])
#
# pc.set_countries()
# print (pc.countries) #['United States']
#
# pc.set_regions()
# print (pc.regions) #['Ohio']
#
# pc.set_cities()
# print (pc.cities) #['Cleveland']
#
# print (pc.address_strings) #['Cleveland, Ohio, United States']
