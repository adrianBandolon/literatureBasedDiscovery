from Data.Structures.ParsedAbstractSummary import ParsedAbstractSummary
import string


class ParsedAbstractSummaryFactory:
    def __init__(self, token_stemmer):
        self.__token_stemmer = token_stemmer

    def build(self, abstract_summary):
        abstract = abstract_summary.abstract
        encoded_abstract = abstract.encode('utf-8').translate(None, string.punctuation)
        unicode_abstract = unicode(encoded_abstract, 'utf-8')
        stemmed_text = self.__token_stemmer.stem(unicode_abstract)
        parsed_abstract = stemmed_text.encode('ascii', 'ignore').split()

        encoded_title = abstract_summary.title.encode('ascii', 'ignore')
        encoded_author = abstract_summary.author.encode('ascii', 'ignore')
        return ParsedAbstractSummary(encoded_title, encoded_author, parsed_abstract)