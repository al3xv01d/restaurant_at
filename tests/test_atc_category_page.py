from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from app.tools import get, find
from config import base_url

def test_add_one_product_to_cart():
    get(base_url + '/bloomfield-commercial-coffee-makers-brewers-pourover')

    category_page = CategoryPage(5)
    title = category_page.product_title.text
    category_page.add_to_cart(1)

    # now we are on cart page

    cart_qty = int(find('//input[@title="Qty"]').get_attribute('value'))
    title_in_cart = find('//table//strong[@class="product-item-name"]/a').text

    assert cart_qty == 1
    assert title == title_in_cart

def test_add_multiple_product_to_cart():
    get(base_url + '/bloomfield-commercial-coffee-makers-brewers-pourover')

    category_page = CategoryPage(5)
    title = category_page.product_title.text
    qty = 12
    category_page.add_to_cart(qty)

    # now we are on cart page

    cart_qty = int(find('//input[@title="Qty"]').get_attribute('value'))
    title_in_cart = find('//table//strong[@class="product-item-name"]/a').text

    assert cart_qty == qty
    assert title == title_in_cart