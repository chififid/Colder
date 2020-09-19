from framework.urls import Urls
from views import home


def init_urls():
    urls = Urls()

    urls.add_path('/test', home)
    urls.add_path('/test', home)

    return urls
