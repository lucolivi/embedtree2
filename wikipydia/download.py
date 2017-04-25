import requests
from . import exceptions

#PageRequestTimeout = exceptions.PageRequestTimeout
#PageDoesNotExists = exceptions.PageDoesNotExists

#from exceptions import PageRequestTimeout, PageDoesNotExists

def _download_page_data(page, lang, timeout):
    """Function to retrieve a wikipedia page in html form, with its sections"""
    #import exceptions


    # https://en.wikipedia.org/w/api.php?action=parse&redirects&page=fluid_mechanics

    req_params = [
        'action=parse',
        'redirects',
        'format=json',
        'prop=text|displaytitle',
        'page=' + page
    ]

    wikipedia_api_url = "https://" + lang + ".wikipedia.org/w/api.php?" + "&".join(req_params)

    try:
        page_data = requests.get(wikipedia_api_url, timeout=timeout).json()
    except requests.exceptions.ConnectTimeout:
        raise exceptions.PageRequestTimeout(page, lang, timeout)

    #If the object parse is not in the json object, page does not exists
    if not 'parse' in page_data:
        raise exceptions.PageDoesNotExists(page, lang)

    page_title = page_data['parse']['title']
    page_id = page_data['parse']['pageid']
    page_html = page_data['parse']['text']['*']

    return page, page_title, page_id, page_html
