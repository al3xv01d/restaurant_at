from app.tools import get, Wait
from config import product, base_url

from time import sleep


def test_add_one_product_to_cart(app):
    get(product)
    title = app.product_page.product_title.text

    app.product_page.add_to_cart()

    Wait.visible(app.product_page.minicart_popup_lo)
    assert '1 item(s) added to your cart' == app.product_page.minicart_popup.title.text
    assert title == app.product_page.minicart_popup.product_link.text
    app.product_page.minicart_popup.view_cart_link.click()

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

    Wait.visible(app.product_page.minicart_popup_lo)
    assert str(qty) + ' item(s) added to your cart' == app.product_page.minicart_popup.title.text
    assert title == app.product_page.minicart_popup.product_link.text
    app.product_page.minicart_popup.view_cart_link.click()

    #now we are on cart page

    cart_qty = int( app.cart_page.item().qty.get_attribute('value') )
    title_in_cart = app.cart_page.item().title.text

    assert cart_qty == qty
    assert title == title_in_cart




