# Literature Based Discovery

## Background:
- This is an attempt at automating Swanson's Literature Based Discovery Method.
- This project was undertaken by: Adrian Bandolon, Menyu Xie, Jun Liang, Michael Wang 

### Package Dependencies:
* os
* gensim
* Biopython
* codecs
* sys
* string
* unicodedata
* nltk
* xml.etree.cElementTree


# test-query-to-feature
`fileparser.py` is the main script, `fileparser()` input a query term and output relavent articles' feature lists.
inside the file there are 3 test queries. run the script to return a list object.

**example output:**

{'Abstract': ['a',
   'deep',
   'understand',
   'immun',
   'landscap',
   'human',
   'cancer',
   'essenti',
   'guid',
   'develop',
   'immunotherapi',
   'benefit',
   'patient',
   'longlast',
   'efficaci',
   'now',
   'two',
   'studi',
   'lavin',
   'al',
   'chevrier',
   'al',
   'employ',
   'mass',
   'cytometri',
   'studi',
   'immun',
   'infiltr',
   'lung',
   'adenocarcinoma',
   'clear',
   'cell',
   'renal',
   'cell',
   'carcinoma',
   'respect'],
  'ArticleTitle': 'Heavy Metal Enlightens Tumor Immunity.',
  'Author': 'Chen Jonathan H'}


#### Helper scripts
`AutoQuery.py` returns xml object contains 200 most relavent articles from term retrieval

`GetAbstract.py` generates a list of article information(title, author, abstract) from the xml object

`FeatureExtraction.py` extracts features from abstract, update to the list of article

##### FeatureExtract.py
`parseOutText()` is the feature extract function using pubmed stopwords and 
`nltk SnowballStemmer`, it calls helper function `remove_punctuation()` to strip off punctuations.

`ProcessFile()` currently take two text collections under this file and read in as utf-8 string, process data through calling `parseOutText()`. It returns a dictionary, of which keys are text file titles and values are list of string(extracted features of that textfile)

##### test-file-to-feature
This folder is to test `fileparser.py`, run this script, it will read in sample `.xml` file in this folder and returns a list object. 

Each item in the list is a dictionary, here is an example:

{'Abstract': ['a',
   'deep',
   'understand',
   'immun',
   'landscap',
   'human',
   'cancer',
   'essenti',
   'guid',
   'develop',
   'immunotherapi',
   'benefit',
   'patient',
   'longlast',
   'efficaci',
   'now',
   'two',
   'studi',
   'lavin',
   'al',
   'chevrier',
   'al',
   'employ',
   'mass',
   'cytometri',
   'studi',
   'immun',
   'infiltr',
   'lung',
   'adenocarcinoma',
   'clear',
   'cell',
   'renal',
   'cell',
   'carcinoma',
   'respect'],
  'ArticleTitle': 'Heavy Metal Enlightens Tumor Immunity.',
  'Author': 'Chen Jonathan H'}
  
  `GetAbstract.py` and `FeatureExtraction.py` contains helper functions that will be called when you run `fileparser.py`
  
  Two stopword lists included: swanson, pubmed
