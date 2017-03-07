from app.tools import get
from config import product

from time import sleep


def test_add_one_product_to_cart(app):
    get(product)
    title = app.product_page.product_title.text

    app.product_page.add_to_cart()

    # now we are on cart page

    cart_qty = int( app.cart_page.item().qty.get_attribute('value') )
    title_in_cart = app.cart_page.item().title.text

    assert cart_qty == 1
    assert title == title_in_cart



def test_add_multiple_product_to_cart(app):
    get(product)
    qty = 11
    title = app.product_page.product_title.text

    app.product_page.add_to_cart(qty)

    #now we are on cart page

    cart_qty = int( app.cart_page.item().qty.get_attribute('value') )
    title_in_cart = app.cart_page.item().title.text

    assert cart_qty == qty
    assert title == title_in_cart




