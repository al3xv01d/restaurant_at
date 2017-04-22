from app.tools import get, Wait
from config import product

# tax == 6.35%


def test_add_one_product_to_cart(app):
    get(product)

    app.product_page.add_to_cart()
    Wait.visible(app.product_page.minicart_popup_lo)
    app.product_page.minicart_popup.view_cart_link.click()

    # now we are on cart page
    app.cart_page.enter_zip('06001')

    product_price = float(app.cart_page.item().price.text[1:])

    Wait.invisible(app.cart_page.tax_price_lo)
    Wait.visible(app.cart_page.tax_price_lo)

    tax = float(app.cart_page.tax_price.text[1:])

    assert tax == ( round((product_price / 100) * 6.35, 2) )