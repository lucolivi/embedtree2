import download
import parse

from wikiarticle import WikiArticle

import wikipedia

from wikidb import WikiDb

if __name__ == "__main__":

    def test_module():
        href, title, pageid, html = _download_page_data("MQTT", "en", 60)
        links = _extract_html_links(html)
        filtered_links = _filter_wiki_links(links)

        for sec in __split_html_h2_sections(_remove_page_boxes(html)):
            print("")
            print(sec)
            #for s in sec:
                #print("")
                #print(s)
        #print(filtered_links)

    def test_wikiarticle():
        href, title, pid, html = download._download_page_data("c%2b%2b", "en", 60)
        wa = WikiArticle(title, pid, html)

        print(wa.title)
        print(wa.page_id)
        
        for l in wa.links():
            print(l)

    def test_wikipedia():
        print(wikipedia.get_article_by_href("c%2b%2b").title)
        print(wikipedia.get_article_by_href("c++").title)
        print(wikipedia.get_article_by_title("c++").title)
        print(wikipedia.get_article_by_title("c%2b%2b").title)

    def test_wikidb():
        db = WikiDb()

        print(db.get_article_by_href("c%2b%2b"))

        db.save()

    test_wikidb()