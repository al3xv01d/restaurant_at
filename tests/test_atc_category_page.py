from app.tools import get
from config import category

def test_add_one_product_to_cart(app):
    get(category)

    title = app.category_page.product_title().text
    app.category_page.add_to_cart(1)

    # now we are on cart page

    cart_qty = int(app.cart_page.item_qty().get_attribute('value'))
    title_in_cart = app.cart_page.item_title().text

    assert cart_qty == 1
    assert title == title_in_cart

def test_add_multiple_product_to_cart(app):
    get(category)

    title = app.category_page.product_title().text
    qty = 12
    app.category_page.add_to_cart(1, qty)

    # now we are on cart page

    cart_qty = int(app.cart_page.item_qty().get_attribute('value'))
    title_in_cart = app.cart_page.item_title().text

    assert cart_qty == qty
    assert title == title_in_cart