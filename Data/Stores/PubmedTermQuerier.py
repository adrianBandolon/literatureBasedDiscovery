class PubmedTermQuerier:
    def __init__(self, entrez, pubmed_db_config):
        self.__entrez = entrez
        self.__db = pubmed_db_config['db']
        self.__sort = pubmed_db_config['sort']
        self.__retmax = pubmed_db_config['retmax']
        self.__retmode = pubmed_db_config['retmode']

    def query_matching_paper_ids(self, term):
        handle = self.__entrez.esearch(
            db=self.__db,
            sort=self.__sort,
            retmax=self.__retmax,
            retmode=self.__retmode,
            term=term)
        results = self.__entrez.read(handle)
        return results['IdList']
