
#!/usr/bin/env python2
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




##create two stopword lists
def swansonStoplist():
    with codecs.open('stopwords_swanson.txt','r', encoding='utf-8') as f:
        swanson = f.readlines()
    swanson = [x.strip() for x in swanson] 
    return swanson

def pubmedStoplist():    
    with codecs.open('stopwords_pubmed.txt','r', encoding='utf-8') as f:
        pubmed = f.readlines()
    pubmed = [x.strip() for x in pubmed]     
    return pubmed





##tokenize and stem unicode string, returns a clean unicode string
def TokenStemmer(f):
                
    new_content=word_tokenize(f)
    
    #stemmer and stopwords
    stemmer = SnowballStemmer("english",ignore_stopwords=False)    
    swansonstopWords=stopwords.words('english')+swansonStoplist()
    pubmedstopWords=stopwords.words('english')+pubmedStoplist()
        

    ##iterate through content word list, skip pubmed stop words and do stemming
    words=''
    for i in new_content:
        if i not in pubmedstopWords:
            new=stemmer.stem(i)
            words=words+' '+new
    return words
