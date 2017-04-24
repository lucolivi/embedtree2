from . import parse

class WikiArticle:
    def __init__(self, title, page_id, html):
        self.title = title
        self.page_id = page_id
        self._html = parse._remove_page_boxes(html)

    def text(self):
        return parse._get_html_text(self._html)
    
    def html(self):
        return self._html

    def links(self):
        return parse._filter_wiki_links(parse._extract_html_links(self._html))

    def __str__(self):
        return self.title