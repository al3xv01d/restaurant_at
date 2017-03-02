from pages.product_page import ProductPage
from app.tools import get, Wait
from config import base_url


def test_add_one_product_from_related_products_block():
    get(base_url + '/bloomfield-8774-a')
    pp = ProductPage()
    pp.add_related()

    Wait.visible(pp.cart_counter_number_lo)
    Wait.visible(pp.related_message_lo)
    Wait.visible(pp.related_modal_lo)

    assert pp.related_title().text in pp.related_modal.text
    assert int(pp.cart_counter_number.text) == 1
    assert pp.related_title().text in pp.related_message.text


def test_add_multiple_product_from_related_products_block():
    get(base_url + '/bloomfield-8774-a')
    pp = ProductPage()
    qty = 5
    pp.add_related(1, qty)

    Wait.visible(pp.cart_counter_number_lo)
    Wait.visible(pp.related_message_lo)
    Wait.visible(pp.related_modal_lo)

    assert pp.related_title().text in pp.related_modal.text
    assert int(pp.cart_counter_number.text) == qty
    assert pp.related_title().text in pp.related_message.text







