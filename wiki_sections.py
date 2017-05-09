
# coding: utf-8

# In[1]:

#from wikipydia import dict_storage, wikidb, parse, wikisyn
from bs4 import BeautifulSoup
import re


# In[2]:

#wiki_db = wikidb.WikiDb()


# In[3]:

class ArticleSection:
    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        
        self._subsections = list()
    
    def add_subsection(self, subsection):
        assert isinstance(subsection, ArticleSection)
        self._subsections.append(subsection)

    def flatten_sections(self):
        """Function to tranverse article hierarchy and place every section into an array."""
        
        flat_sections = list()
        flat_sections.append(self)

        for sec in self._subsections:
            for flat_sec in sec.flatten_sections():
                flat_sections.append(flat_sec)

        return flat_sections


    def __iter__(self):
        return self._subsections.__iter__()

    def __getitem__(self, index):
        assert index > 0
        return self._subsections[index-1]
    
    def __str__(self):
        content_list = list()
        content_list.append(self.title)
        content_list.append(self.content)

        for subsec in self._subsections:
            content_list.append(str(subsec))

        return "\n".join(content_list)
    
#section = ArticleSection("MQTT", "ae")
#subsec1 = ArticleSection("Test1", "sduiuha")
#section.add_subsection(subsec1)
#print(section[1][0])


# In[4]:

def get_htag_value(tag_name):
    """Function to return the h tag value in case tag is a h tag."""
    
    try:
        assert len(tag_name) == 2
        assert tag_name.lower()[0] == "h"
        assert int(tag_name[1]) > 0
        return int(tag_name[1])
    except:
        return -1
    
# assert get_htag_value("h1") == 1
# assert get_htag_value("h9") == 9
# assert get_htag_value("H3") == 3
# assert get_htag_value("H7") == 7
# assert get_htag_value("h10") == -1
# assert get_htag_value("h0") == -1
# assert get_htag_value("p6") == -1
# assert get_htag_value("sh6") == -1
# assert get_htag_value("SOIS") == -1
# print("Test OK")


# In[5]:

#art, _ = wiki_db.get_article_by_href("Deep_learning")


# In[6]:

def get_tag_text(tag):
    regex_remove_list = [
        '\[edit\]',
        '\[[0-9]+\]'
    ]
    
    tag_text = tag.get_text()
    
    for expr in regex_remove_list:
        tag_text = re.sub(expr, "", tag_text)
        
    return tag_text


# In[7]:

def get_article_sections_list(title, html):
    soup = BeautifulSoup(html, 'html.parser')
    
    sections = list()
    
    curr_section = dict()
    sections.append(curr_section)

    curr_section['title'] = title
    curr_section['content'] = ""
    curr_section['h'] = 1

    for tag in soup.children:

        #If it is a valid tag (invalid tags has no 'name' property)
        if tag.name == None:
            continue
            
        htag_value = get_htag_value(tag.name)
        
        if htag_value > 0:
            curr_section = dict()
            sections.append(curr_section)

            curr_section['title'] = get_tag_text(tag)
            curr_section['content'] = ""
            curr_section['h'] = htag_value
            
        else:    
            curr_section['content'] += get_tag_text(tag)
            
    return sections

#test_sections = get_article_sections_list(art.title(),art.html())

#for test_sec in test_sections:
    #print(test_sec['title'])


# In[8]:

def get_article_obj(title, html):
    """Function to split html document in sections (use h tags as divisors)"""
    
    sections = get_article_sections_list(title, html)
    
    
    last_sections = dict()

    curr_title = title
    curr_content = ""
    curr_htag_value = 1
    
    sections = get_article_sections_list(title, html)

    for sec in sections:
        new_section = ArticleSection(sec['title'], sec['content'])
        
        htag_value = sec['h']
        last_sections[htag_value] = new_section
        
        #If it is not the top section, append to its parent
        if htag_value > 1:
            last_sections[htag_value-1].add_subsection(new_section)
    
    return last_sections[1]


#test_article = get_article_obj(art.title(),art.html())


# In[9]:

#print(test_article)


# In[ ]:

def dep_split_html_h2_sections(html):
    """Function to split html document in sections (use h2 tags as divisors)"""

    soup = BeautifulSoup(html, 'html.parser')

    sections = list()

    curr_section = ""

    for tag in soup.children:

        #If it is a valid tag (invalid tags has no 'name' property)
        if tag.name == None:
            continue

        #Start new section in case the tag is h2
        if tag.name == 'h2':
            sections.append(curr_section)
            curr_section = ""

        curr_section += str(tag)

    sections.append(curr_section) #Append final section

    return sections


# In[10]:

#art, _ = wiki_db.get_article_by_href("MQTT")
#print(art.html())


# In[ ]:



