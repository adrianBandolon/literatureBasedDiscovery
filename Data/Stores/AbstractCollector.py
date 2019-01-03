import copy


class AbstractCollector:
    def __init__(self, pubmed_article_querier, abstract_summary_factory, parsed_abstract_summary_factory):
        self.__store = []
        self.__pubmed_article_querier = pubmed_article_querier
        self.__abstract_summary_factory = abstract_summary_factory
        self.__parsed_abstract_summary_factory = parsed_abstract_summary_factory

    def snapshot_store(self):
        return copy.deepcopy(self.__store)

    def collect_abstracts_matching_term(self, term):
        article_query_results = self.__pubmed_article_querier.query(term)

        for article_result in article_query_results:
            try:
                abstract_summary = self.__abstract_summary_factory.build(article_result)
            except KeyError as ke:
                print 'abstract cannot be built because abstract is missing: %s' % ke
                continue

            parsed_abstract_summary = self.__parsed_abstract_summary_factory.build(abstract_summary)
            self.__store.append(parsed_abstract_summary)
