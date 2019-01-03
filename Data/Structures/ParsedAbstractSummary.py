class ParsedAbstractSummary:
    def __init__(self, title, author, parsed_abstract):
        self.title = title
        self.author = author
        self.parsed_abstract = parsed_abstract

    def __str__(self):
        unicode_string = '%s wrote %s: %s' % (self.author, self.title, self.parsed_abstract)
        return unicode_string.encode('ascii', 'ignore')