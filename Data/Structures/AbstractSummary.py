class AbstractSummary:
    def __init__(self, title, author, abstract):
        self.title = title
        self.author = author
        self.abstract = abstract

    def __str__(self):
        return '%s wrote %s: %s' % (self.author, self.title, self.abstract)