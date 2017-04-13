from . import wikiarticle, download

WikiArticle = wikiarticle.WikiArticle

import urllib

def get_article_by_href(href, lang='en', timeout=60):
    href, title, pid, html = download._download_page_data(href, lang, timeout)
    return WikiArticle(title, pid, html)

def get_article_by_title(title, lang='en', timeout=60):
    return get_article_by_href(urllib.parse.quote(title), lang, timeout)