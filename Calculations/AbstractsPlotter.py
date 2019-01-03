

class AbstractsPlotter:
    def __init__(self, abstracts_tagger, abstracts_vectorizer, abstract_points_collector):
        self.__abstracts_tagger = abstracts_tagger
        self.__abstracts_vectorizer = abstracts_vectorizer
        self.__abstract_points_collector = abstract_points_collector


    def plot(self, abstracts):
        tagged_abstracts = self.__abstracts_tagger.tag(abstracts)
        vectorized_abstracts = self.__abstracts_vectorizer.vectorize(tagged_abstracts)
        t_sne_points = self.__abstract_points_collector.collect(vectorized_abstracts)
        return t_sne_points
