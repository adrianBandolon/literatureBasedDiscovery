#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 02:54:09 2017

@author: mengyuxie
"""
import os
import codecs
import sys  
import string
import unicodedata
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize



##remove unicode punctuation
tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                      if unicodedata.category(unichr(i)).startswith('P'))
print tbl
def remove_punctuation(text):
    return text.translate(tbl)




##create two stopword lists
with codecs.open('stopwords_swanson.txt','r', encoding='utf-8') as f:
    swanson = f.readlines()
swanson = [x.strip() for x in swanson] 

with codecs.open('stopwords_pubmed.txt','r', encoding='utf-8') as f:
    pubmed = f.readlines()
pubmed = [x.strip() for x in pubmed]



def parseOutText(f):
                
    f.seek(0) 
    content = f.read()
    
    ##remove punctuation followed by tokenize 
    content=remove_punctuation(content)
    new_content=word_tokenize(content)
    
    #stemmer and stopwords
    stemmer = SnowballStemmer("english",ignore_stopwords=False)    
    swansonstopWords=stopwords.words('english')+swanson
    pubmedstopWords=stopwords.words('english')+pubmed
        

    ##iterate through content word list, skip pubmed stop words and do stemming  
    words=''
    for i in new_content:
        if i not in pubmedstopWords:
            new=stemmer.stem(i)
            words=words+' '+new
    return words
        


   
    
    
def ProcessFile():
    ab_dict = {}        
    fish_oil_filepath = "collections-of-abstracts/FishOilAbstracts/"
    raynauds_filepath = "collections-of-abstracts/RaynaudsDiseaseAbstracts/"
    for directory in [fish_oil_filepath, raynauds_filepath]:
        for file_name in os.listdir(directory):
            #ab_dict[file_name]=text
            #print file_name
            full_file_path = directory + file_name
            #inst_dict.append(full_file_path)
            ff = codecs.open(full_file_path, 'r', encoding='utf-8')
            text = parseOutText(ff)
            text=unicodedata.normalize('NFKD', text).encode('ascii','ignore')
            ab_dict[file_name[:-4]]=text.split()
    return ab_dict      
    

print ProcessFile()





