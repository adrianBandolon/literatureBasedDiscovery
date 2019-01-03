from gensim.models.doc2vec import Doc2Vec
import numpy as np


class AbstractsVectorizer:
    def __init__(self):
        pass

    def vectorize(self, tagged_abstracts):
        model = Doc2Vec(tagged_abstracts, seed=0)
        document_vectors = model.docvecs
        return document_vectors
