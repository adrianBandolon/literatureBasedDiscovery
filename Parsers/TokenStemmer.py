from nltk.tokenize import word_tokenize


class TokenStemmer:
    def __init__(self, stemmer, stop_word_list):
        self.__stemmer = stemmer
        self.__stop_word_list = stop_word_list

    def stem(self, unicode_text):
        tokenized_text = word_tokenize(unicode_text)
        stemmed_text  = ''
        for i in tokenized_text:
            if i not in self.__stop_word_list:
                stemmed_word = self.__stemmer.stem(i)
                stemmed_text += '%s ' % stemmed_word
        return stemmed_text