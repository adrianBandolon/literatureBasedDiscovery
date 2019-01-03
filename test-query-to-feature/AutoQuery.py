
from Bio import Entrez
from Bio.Entrez import efetch
# must install biopython package
# pip install biopython

# returns a list of citation IDs in ['IdList] using esearch utility
def search(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='200', # current limit is 200, could download more if done in blocks
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

# uses the id_list to query pubmed using efetch utility
def fetch_abstract(id_list):
    ids = ','.join(id_list)
    handle = efetch(db='pubmed', id=ids, retmode='xml') ### this step returns xml object
    #results = Entrez.read(handle) #this step read xml to string
    #return results
    return handle


def GetQuery(term):
    #arbitrary search term for now (incorporate into front end?)
    results = search(term)
    id_list = results['IdList']
    papers = fetch_abstract(id_list)

    return papers ##returns a xml object, which is taken by the parser as input

