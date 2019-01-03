import numpy as np


class AbstractPointsArrayCreator:
    def __init__(self, t_sne):
        self.__t_sne = t_sne

    def create(self, vectorized_abstracts):
        abstract_vectors_list = []
        for doc_vec in vectorized_abstracts:
            abstract_vectors_list.append(doc_vec)

        abstract_vectors_array = np.vstack(abstract_vectors_list)
        abstract_points_array = self.__t_sne.fit_transform(abstract_vectors_array)
        return abstract_points_array