import pickle

from collections import Counter, defaultdict

"""
WIKISYN WILL HELP IN THE FUTURE TO ASSIGN DOCUMENTS, CLASSES TO WIKIPEDIA ARTICLES


"""




"""
def load(filename):
    pass

def save(filename):
    with open(self.filename, mode='r+b') as pickle_file:
        saved_data = pickle.load(pickle_file)
                
                self.submitted_pageids = saved_data.submitted_pageids
                self.hrefs = saved_data.hrefs


class WikisynbetaDict:
    def __init__(self, filename):
        self.filename = filename + ".pickle"
        
        self.submitted_pageids = set()
        self.hrefs = dict()
        
        try:
            with open(self.filename, mode='r+b') as pickle_file:
                saved_data = pickle.load(pickle_file)
                
                self.submitted_pageids = saved_data.submitted_pageids
                self.hrefs = saved_data.hrefs
                
        except IOError:
            print("Failed to open " + self.filename + ". Created empty wikisyn.")
        
    def save(self):
        with open(self.filename, mode='w+b') as pickle_file:
            pickle.dump(self, pickle_file)
    

    
    def get_joined_synoms(self, page_hrefs, norm=True):
        
        synoms = dict()
        
        norm_fact = 0
        
        for href in page_hrefs:
            if href not in self.hrefs:
                continue
            for l_text, l_score in self.hrefs[href].items():
                
                if l_text not in synoms:
                    synoms[l_text] = 0
                
                synoms[l_text] += l_score
                norm_fact += l_score                
        
        #If we should not return scores normalized
        if not norm:
            return synoms.items()
        
        norm_synoms = list()
        for text, score in synoms.items():
            norm_synoms.append((text, score / norm_fact))
        
        return norm_synoms
"""
class WikisynDict(defaultdict):
    """Class to compute wikisyns."""

    def __init__(self):
        super(WikisynDict, self).__init__(Counter)

    def add_link(self, link_href, link_text):
        """Add a link to the wikisyn dict. """

        #If the link_text is invalid (empty, spaces etc) skip it
        if not link_text:
            return

        href_texts = super(WikisynDict, self).__getitem__(link_href)
        href_texts[link_text] += 1

    def __getitem__(self, href):

        norm_fact = 0
        for text, score in super(WikisynDict, self).__getitem__(href).items():
            norm_fact += score

        norm_synoms = list()
        for text, score in super(WikisynDict, self).__getitem__(href).items():
            #norm_synoms.append((text, float(score) / norm_fact))
            norm_synoms.append((text, round(score / norm_fact, 2)))

        return norm_synoms



    

#Test
if __name__ == '__main__':
    #from wikipedia import get_article_by_href
    #wikiart = get_article_by_href("MQTT")
    test_dict = WikisynDict()

    test_dict.add_link("link1", "text1")
    test_dict.add_link("link1", "text1")
    test_dict.add_link("link1", "text2")
    test_dict.add_link("link2", "text3")
    test_dict.add_link("link3", "text3")

    print(test_dict["link1"])
    print(test_dict["link2"])
    print(test_dict["asdfsa"])

    print(test_dict)