from wikipydia import dict_storage, wikidb, parse, wikisyn


def local_wikisyn(href):
    pass



def get_href_text_count(href):
    synDict = WikisynDict()

    wikiart, _ = wiki_db.get_article_by_href(href)
    links = wikiart.links()
    page_text = wikiart.text()
    
    #Populate syndict
    for href, text in links:
        synDict.add_link(href, text)
        
    #Get matches
    links_score = Counter()
        
    for link_href in synDict.keys():
        for l_text, l_score in synDict[link_href]:
            matches = re.findall('[^a-zA-Z0-9_]' + re.escape(l_text) + '[^a-zA-Z0-9_]', page_text, re.IGNORECASE)
            matches_score = len(matches) * l_score
            links_score[link_href] += matches_score

    scores_sum = sum(links_score.values())
            
    #norm_links_scores = list(map(lambda a: (a[0],synDict[a[0]], a[1]/scores_sum), links_score.most_common()))
    #norm_links_scores = list(map(lambda a: (a[0], a[1]/scores_sum), links_score.most_common()))
    norm_links_scores = list(map(lambda a: (a[0],list(map(lambda b: b[0], synDict[a[0]])), a[1]/scores_sum), links_score.most_common()))
    
    return norm_links_scores