from . import parse

class WikiArticle:
    def __init__(self, title, page_id, html):
        self._title = title
        self._page_id = page_id
        self._html = html

    def text(self):    
        html_data = self.html()
        html_text = parse._get_html_text(html_data)
        return html_text
    
    def html(self):
        parsed_html = parse._remove_page_boxes(self._html)
        parsed_html = parse._remove_informationless_sections(parsed_html)
        return parsed_html 

    def links(self):
        html_data = self.html()
        html_links = parse._extract_html_links(html_data)
        html_links = parse._filter_wiki_links(html_links)
        return html_links

    def title(self):
        return self._title

    def page_id(self):
        return self._page_id

    def __str__(self):
        return self._title

if __name__ == "__main__":
    import download
    href, title, pid, html = download._download_page_data("MQTT", "en", 60)
    wikiart = WikiArticle((title, pid, html))
    assert wikiart.title() == "MQTT"
    assert wikiart.page_id() == 32695816
    assert len(wikiart.links()) == 25

    print("All tests passed.")

    print([wikiart.text()])