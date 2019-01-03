from Bio.Entrez import efetch


class PubmedArticleQuerier:
    def __init__(self, term_querier, entrez, pubmed_db_config):
        self.__term_querier = term_querier
        self.__entrez = entrez
        self.__db = pubmed_db_config['db']
        self.__retmode = pubmed_db_config['retmode']

    def query(self, term):
        id_list = self.__term_querier.query_matching_paper_ids(term)
        id_list_string = ','.join(id_list)
        handle = efetch(db=self.__db, id=id_list_string, retmode=self.__retmode)
        papers = self.__entrez.read(handle)
        return papers['PubmedArticle']
