from pages.index import IndexPage
from pages.cart_page import CartPage
from app.tools import get, find
from config import base_url

def test_add_one_product_to_cart():
    get(base_url)
    index = IndexPage()
    index.find('star')


def test_add_multiple_product_to_cart():
    pass
