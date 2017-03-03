from app.tools import get, find
from config import base_url

def test_add_one_product_to_cart(app):
    get(base_url)

    app.search_page.find('star')
    title = app.search_page.item_title().get_attribute('title')
    app.search_page.add_to_cart()

    cart_qty = int(app.cart_page.item_qty().get_attribute('value'))
    title_in_cart = app.cart_page.item_title().text

    assert cart_qty == 1
    assert title == title_in_cart


def test_add_multiple_product_to_cart(app):
    get(base_url)

    app.search_page.find('star')
    title = app.search_page.item_title().get_attribute('title')
    qty = 15
    app.search_page.add_to_cart(1, qty)

    cart_qty = int(app.cart_page.item_qty().get_attribute('value'))
    title_in_cart = app.cart_page.item_title().text

    assert cart_qty == qty
    assert title == title_in_cart
