from app.tools import get, Wait
from config import product_with_related


def test_add_one_product_from_related_products_block(app):
    get(product_with_related)
    app.product_page.add_related()

    Wait.visible(app.product_page.cart_counter_number_lo)
    Wait.visible(app.product_page.related_message_lo)
    Wait.visible(app.product_page.related_modal_lo)

    assert app.product_page.related().title.text in app.product_page.related_modal.text
    assert int(app.product_page.cart_counter_number.text) == 1
    assert app.product_page.related().title.text in app.product_page.related_message.text


def test_add_multiple_product_from_related_products_block(app):
    get(product_with_related)
    qty = 5
    app.product_page.add_related(qty)

    Wait.visible(app.product_page.cart_counter_number_lo)
    Wait.visible(app.product_page.related_message_lo)
    Wait.visible(app.product_page.related_modal_lo)

    assert app.product_page.related().title.text in app.product_page.related_modal.text
    assert int(app.product_page.cart_counter_number.text) == qty
    assert app.product_page.related().title.text in app.product_page.related_message.text







