from pages.product_page import ProductPage
from pages.cart_page import CartPage
from app.tools import get, find
from config import base_url

from time import sleep


def test_add_one_product_to_cart():
    get(base_url + '/bloomfield-8774-a')
    pp = ProductPage()
    title = pp.product_title.text

    pp.add_to_cart()

    # now we are on cart page
    cart_page = CartPage()
    cart_qty = int( cart_page.item_qty.get_attribute('value') )
    title_in_cart = cart_page.item_title.text

    assert cart_qty == 1
    assert title == title_in_cart



def test_add_multiple_product_to_cart():
    get(base_url + '/bloomfield-8774-a')
    pp = ProductPage()
    qty = 11
    title = pp.product_title.text

    pp.add_to_cart(qty)

    #now we are on cart page
    cart_page = CartPage()
    cart_qty = int(cart_page.item_qty.get_attribute('value'))
    title_in_cart = cart_page.item_title.text

    assert cart_qty == qty
    assert title == title_in_cart




