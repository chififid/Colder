from .errors import *


class Urls:
    def __init__(self):
        self.URLS = {}

    def add_path(self, url, function):
        self.URLS[url] = function

    def generate_content(self, url, method):
        if '?' in url:
            url, response = url.split('?')[0], url.split('?')[1]

            if not url in self.URLS:
                return error('404')

            return ('HTTP/1.1 200 ОК\n\n' + self.URLS[url](method, response)).encode()

        if not url in self.URLS:
            return error('404')

        return ('HTTP/1.1 200 ОК\n\n' + self.URLS[url](method)).encode()
