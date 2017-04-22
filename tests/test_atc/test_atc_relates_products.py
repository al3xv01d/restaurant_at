from app.tools import get, Wait
from config import product_with_related
from time import sleep

def test_add_one_product_from_related_products_block(app):
    get(product_with_related)
    rel_title = app.product_page.related().title.text
    app.product_page.add_related()

    Wait.visible(app.product_page.minicart_popup_lo)
    assert '1 item(s) added to your cart' == app.product_page.minicart_popup.title.text
    assert rel_title == app.product_page.minicart_popup.product_link.text

    assert int(app.product_page.cart_counter_number.text) == 1

    sleep(1)
    app.product_page.minicart_popup.view_cart_link.click()

    cart_qty = int(app.cart_page.item().qty.get_attribute('value'))
    title_in_cart = app.cart_page.item().title.text

    assert cart_qty == 1
    assert rel_title == title_in_cart


def test_add_multiple_product_from_related_products_block(app):
    get(product_with_related)
    qty = 5
    rel_title = app.product_page.related().title.text
    app.product_page.add_related(1, qty)

    Wait.visible(app.product_page.minicart_popup_lo)
    assert str(qty) + ' item(s) added to your cart' == app.product_page.minicart_popup.title.text
    assert rel_title == app.product_page.minicart_popup.product_link.text

    assert int(app.product_page.cart_counter_number.text) == qty

    sleep(1)
    app.product_page.minicart_popup.view_cart_link.click()

    cart_qty = int(app.cart_page.item().qty.get_attribute('value'))
    title_in_cart = app.cart_page.item().title.text

    assert cart_qty == qty
    assert rel_title == title_in_cart






