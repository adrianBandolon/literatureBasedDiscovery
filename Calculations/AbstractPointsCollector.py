class AbstractPointsCollector:
    def __init__(self, abstract_points_array_creator):
        self.__abstract_points_array_creator = abstract_points_array_creator

    def collect(self, vectorized_abstracts):
        abstract_points_array = self.__abstract_points_array_creator.create(vectorized_abstracts)

        abstract_vector_collection = {}
        doc_tags = vectorized_abstracts.doctags
        for doc_tag, point in zip(doc_tags, abstract_points_array):
            abstract_vector_collection[doc_tag] = {'x_coordinate': float(point[0]), 'y_coordinate': float(point[1])}
        return abstract_vector_collection
