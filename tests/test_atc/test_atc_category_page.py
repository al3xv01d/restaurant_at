from app.tools import get, Wait
from config import category

def test_add_one_product_to_cart(app):
    get(category)

    title = app.category_page.item().title.text
    app.category_page.add_to_cart(1)

    Wait.visible(app.product_page.minicart_popup_lo)
    assert '1 item(s) added to your cart' == app.product_page.minicart_popup.title.text
    assert title == app.product_page.minicart_popup.product_link.text
    app.product_page.minicart_popup.view_cart_link.click()

    # now we are on cart page

    cart_qty = int(app.cart_page.item().qty.get_attribute('value'))
    title_in_cart = app.cart_page.item().title.text

    assert cart_qty == 1
    assert title == title_in_cart

def test_add_multiple_product_to_cart(app):
    get(category)

    title = app.category_page.item().title.text
    qty = 12
    app.category_page.add_to_cart(qty)

    Wait.visible(app.product_page.minicart_popup_lo)
    assert str(qty) + ' item(s) added to your cart' == app.product_page.minicart_popup.title.text
    assert title == app.product_page.minicart_popup.product_link.text
    app.product_page.minicart_popup.view_cart_link.click()

    # now we are on cart page

    cart_qty = int(app.cart_page.item().qty.get_attribute('value'))
    title_in_cart = app.cart_page.item().title.text

    assert cart_qty == qty
    assert title == title_in_cart