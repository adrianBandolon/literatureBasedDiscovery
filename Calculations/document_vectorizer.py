from DocumentFilepaths import fish_oil_filepath, raynauds_filepath
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
import numpy as np
import os
from sklearn.manifold import TSNE

tagged_documents = []


def get_tagged_documents():
    for directory in [fish_oil_filepath, raynauds_filepath]:
        for file_name in os.listdir(directory):
            full_file_path = directory + file_name
            with open(full_file_path, 'r') as document:
                document_str = document.read()
                words_list = document_str.split(' ')
                tagged_document = TaggedDocument(words_list, [full_file_path])
                tagged_documents.append(tagged_document)
            document.close()
    return tagged_documents


def get_document_vector_array(model):
    document_vector_list = []
    document_vectors = model.docvecs

    for document_vector in document_vectors:
        document_vector_list.append(document_vector)
    return np.asarray(document_vector_list)



tagged_documents = get_tagged_documents()
model = Doc2Vec(tagged_documents, seed=0)
document_vector_array = get_document_vector_array(model)

tsne = TSNE(random_state=0)
tsne_points = tsne.fit_transform(document_vector_array)
for full_document_path, point in zip(model.docvecs.doctags, tsne_points):
    if "FishOilAbstracts" in full_document_path:
        document_type = "FishOilAbstracts"
        document_name = full_document_path[42:]
    else:
        document_type = "RaynaudsDiseaseAbstracts"
        document_name = full_document_path[50:]

    print document_name, document_type, point