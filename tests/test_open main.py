from pages.index import Index
from app.tools import get, find
from config import base_url
from time import sleep

def test_open_page(app):
    get(base_url)
    index = Index()
    index.login()

    index.logout()





# def test_open_news_page(app):
#
#     link = find('//*[@id="tabnews_news"]/h1/a')
#     link.click()