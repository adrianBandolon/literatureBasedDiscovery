import os
import codecs
import sys  
import string
import unicodedata
import xml.etree.cElementTree as ET
import codecs
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from Bio import Entrez
from Bio.Entrez import efetch


from AutoQuery import GetQuery
from GetAbstract import ProccessQuery
from FeatureExtraction import TokenStemmer



def fileparser(term):
    
    xml_object = GetQuery(term)
    sample=ProccessQuery(xml_object)

    feature_list=[]     
    for i in sample:
        if i['Abstract']!=None: #make sure not include missing/bad data point
            content=i['Abstract']
            #translate to string type for punctuation removal
            text_string = content.encode('utf-8').translate(None, string.punctuation)
            #back to unicode
            Utext_string=unicode(text_string, "utf-8")
            #call the TokenStemmer() from FeatureExtraction.py
            text = TokenStemmer(Utext_string)
            #change again back to ascii string type and split into word list
            #text=unicodedata.normalize('NFKD', text).encode('ascii','ignore')
            #change again back to ascii string type and split into word list
            features=text.encode('ascii','ignore').split()
            
            ##update value of 'Abstract' to the feature list
            i['Abstract']=features
            feature_list.append(i)
    return feature_list 
            
            
if __name__ == '__main__':
    sample_query1='((tumor) AND "Cell"[Journal])'
    sample_query2='immunotherapy'
    sample_query2='(HDAC) AND immunotherapy' 
    ablist=fileparser(sample_query2)
    print ablist