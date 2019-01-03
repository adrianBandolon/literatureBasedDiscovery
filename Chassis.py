from Bio import Entrez
import config
import json
from nltk.stem.snowball import SnowballStemmer
from sklearn.manifold.t_sne import TSNE

from Calculations.AbstractPointsArrayCreator import AbstractPointsArrayCreator
from Calculations.AbstractPointsCollector import AbstractPointsCollector
from Calculations.AbstractsPlotter import AbstractsPlotter
from Calculations.AbstractsVectorizer import AbstractsVectorizer
from Data.Stores.AbstractCollector import AbstractCollector
from Data.Stores.PubmedArticleQuerier import PubmedArticleQuerier
from Data.Stores.PubmedTermQuerier import PubmedTermQuerier
from Data.Structures.AbstractSummaryFactory import AbstractSummaryFactory
from Data.Structures.AbstractsTagger import AbstractsTagger
from Data.Structures.ParsedAbstractSummaryFactory import ParsedAbstractSummaryFactory
from Parsers.TokenStemmer import TokenStemmer
from Parsers.PubmedStopWordListFactory import PubmedStopWordListFactory


class Chassis:
    def __init__(self):
        self.__config = config
        self.__abstract_collector = None
        self.__abstracts_plotter = None

    def build(self):
        # create Entrez object
        entrez = Entrez
        entrez.email = self.__config.pubmed_db_config['email']

        # create queriers and stemmers
        pubmed_term_querier = PubmedTermQuerier(entrez, self.__config.pubmed_db_config)
        pubmed_article_querier = PubmedArticleQuerier(pubmed_term_querier, entrez, self.__config.pubmed_db_config)

        abstract_summary_factory = AbstractSummaryFactory()
        snowball_stemmer = SnowballStemmer("english", ignore_stopwords=False)
        pubmed_stop_word_list = PubmedStopWordListFactory().build()
        token_stemmer = TokenStemmer(snowball_stemmer, pubmed_stop_word_list)
        parsed_abstract_summary_factory = ParsedAbstractSummaryFactory(token_stemmer)
        self.__abstract_collector = AbstractCollector(
            pubmed_article_querier,
            abstract_summary_factory,
            parsed_abstract_summary_factory)

        # create document vectorizer
        abstracts_tagger = AbstractsTagger()
        abstracts_vectorizer = AbstractsVectorizer()
        t_sne = TSNE(random_state=0)
        abstract_points_array_creator = AbstractPointsArrayCreator(t_sne)
        abstract_points_collector = AbstractPointsCollector(abstract_points_array_creator)
        self.__abstracts_plotter = AbstractsPlotter(abstracts_tagger, abstracts_vectorizer, abstract_points_collector)

    def run(self):
        while True:
            self.__abstract_collector.collect_abstracts_matching_term(raw_input('term: '))
            abstracts = self.__abstract_collector.snapshot_store()
            abstract_plot = self.__abstracts_plotter.plot(abstracts)
            with open('abstract_plot.json', 'w') as abstract_plot_json:
                json.dump(abstract_plot, abstract_plot_json)
