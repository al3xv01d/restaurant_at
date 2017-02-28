from pages.product_page import ProductPage
from app.tools import get, find
from config import base_url


def test_add_one_product_from_related_products_block():
    get(base_url + '/bloomfield-8774-a')
    pp = ProductPage()









