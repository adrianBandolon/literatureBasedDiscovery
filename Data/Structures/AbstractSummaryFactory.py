from Data.Structures.AbstractSummary import AbstractSummary


class AbstractSummaryFactory:
    def __init__(self):
        pass

    def build(self, article_result):
        med_line_citation = article_result['MedlineCitation']
        article = med_line_citation['Article']

        title = article['ArticleTitle']

        author_list = article['AuthorList']
        first_author = author_list[0]
        first_author_name = first_author['LastName'] + ', ' + first_author['ForeName']

        abstract = article['Abstract']
        abstract_text = abstract['AbstractText']

        if type(abstract_text) == list:
            combined_abstract_text = ''
            for abstract_subtext in abstract_text:
                combined_abstract_text += abstract_subtext
            return AbstractSummary(title, first_author_name, combined_abstract_text)
        else:
            return AbstractSummary(title, first_author_name, abstract_text)
