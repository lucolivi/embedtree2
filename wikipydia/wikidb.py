from . import wikipedia, dict_storage

DictStorage = dict_storage.DictStorage

class WikiDb(object):
    def __init__(self):

        self.href_to_pageid = DictStorage("href_to_pageid") #Storage lookup table of hrefs and pageids
        self.pageid_to_href = DictStorage("pageid_to_href") #Storage lookup table of pageid and hrefs
        self.pageid_to_article = DictStorage("pageid_to_article") #Storage for page titles

    def get_article_by_href(self, href, lang='en', timeout=60):

        downloaded = False

        #Check if the page is in the redirects table, if not, download it and register it
        if not href in self.href_to_pageid:
            #print("Page not found. Downloading and registering it...")
            wikiart = wikipedia.get_article_by_href(href, lang, timeout)
            self._register_page_data(href, wikiart)
            downloaded = True
            #print("Done.")

        page_id = self.href_to_pageid[href]
        return self.pageid_to_article[page_id], downloaded


    def get_article_by_title(title, lang='en', timeout=60):
        return get_article_by_href(urllib.parse.quote(title), lang, timeout)

    def save(self):
        self.href_to_pageid.save()
        self.pageid_to_href.save()
        self.pageid_to_article.save()


    #Function to save page data to storages
    def _register_page_data(self, href, wikiart):

        #Register page id lookup tables
        self.href_to_pageid[href] = wikiart.page_id()

        #Register article
        self.pageid_to_article[wikiart.page_id()] = wikiart

        if not wikiart.page_id() in self.pageid_to_href:
            self.pageid_to_href[wikiart.page_id()] = set()
        self.pageid_to_href[wikiart.page_id()].add(href)

        # #Register page links and wikisyn
        # page_links = get_page_links(page_data)
        # pageid_to_page_links[page_id] = set()
        # for link_href, link_text in page_links:
        #     pageid_to_page_links[page_id].add(link_href)
        #     if not link_href in wikisyn:
        #         wikisyn[link_href] = set()
        #     wikisyn[link_href].add(link_text)
