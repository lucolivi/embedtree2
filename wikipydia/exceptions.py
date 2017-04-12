class PageDoesNotExists(Exception):
    def __init__(self, page, lang):
        super().__init__("Requested page '{0} ({1})' does not exists.".format(page, lang))

class PageRequestTimeout(Exception):
    def __init__(self, page, lang, timeout):
        super().__init__("Timeout ({2}) while requesting page '{0} ({1})'.".format(page, lang, timeout))