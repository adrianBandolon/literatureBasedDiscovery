import xml.etree.cElementTree as ET
import codecs


##read file to the tree
def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

##extract ArticleTitle, Abstract,Author information into a list of dictionary
def get_abstracts(root):
    collection = []
    for article in root.findall("./PubmedArticle/MedlineCitation/Article"):
        data = {
                "ArticleTitle": None,
                "Abstract": None, 
                "Author":None,
        } 
        
        
        ##check the exsitence of those tags for each item, pass if it's None
        check= article.find('./ArticleTitle')==None or article.find('./Abstract/AbstractText')==None or article.find('./AuthorList/Author/LastName')==None or article.find('./AuthorList/Author/ForeName')==None            
        if check==True:
            pass
        else:
            
            
            ##extract as string
            data["ArticleTitle"] = article.find('./ArticleTitle').text
            data["Abstract"] = article.find('./Abstract/AbstractText').text
            data["Author"] = article.find('./AuthorList/Author/LastName').text +' '+ article.find('./AuthorList/Author/ForeName').text
            collection.append(data)
    return collection

    

##call the helper function, returns data as list of dictionary
def ProccessFile(filename):
    root = get_root(filename)
    data = get_abstracts(root)
    return data
    


#if __name__ == '__main__':
#    filename = "sample_pubmed_result.xml"
#    ProccessFile(filename)
