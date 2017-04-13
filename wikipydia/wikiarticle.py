from . import parse

class WikiArticle:
    def __init__(self, title, page_id, html):
        self.title = title
        self.page_id = page_id
        self.html = parse._remove_page_boxes(html)

    def text(self):
        return parse._get_html_text(self.html)

    def links(self):
        return parse._filter_wiki_links(parse._extract_html_links(self.html))

    def __str__(self):
        return self.title