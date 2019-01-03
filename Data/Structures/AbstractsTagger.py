from gensim.models.doc2vec import TaggedDocument


class AbstractsTagger:
    def __init__(self):
        pass

    def tag(self, abstracts):
        tagged_documents = []
        for abstract in abstracts:
            title = abstract.title
            abstract_text = abstract.parsed_abstract
            tagged_document = TaggedDocument(abstract_text, [title])
            tagged_documents.append(tagged_document)
        return tagged_documents