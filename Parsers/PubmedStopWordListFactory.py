import codecs
from nltk.corpus import stopwords


class PubmedStopWordListFactory:
    def __init__(self):
        pass

    def build(self):
        with codecs.open('stopwords_pubmed.txt', 'r', encoding='utf-8') as f:
            pubmed = f.readlines()
        pubmed = [x.strip() for x in pubmed]
        f.close()
        full_stop_word_list = stopwords.words('english') + pubmed
        return full_stop_word_list