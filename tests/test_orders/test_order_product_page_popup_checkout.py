from app.tools import get, Wait
from config import product

def test_order_pp_popup_bs1(app):

    get(product)

    app.product_page.add_to_cart()
    Wait.visible(app.product_page.minicart_popup_lo)
    app.product_page.minicart_popup.checkout_link.click()

    # *****************************on chechout page

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.checkout_page.fill_shipping_form()

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.checkout_page.fill_billing_form(True)
    app.checkout_page.fill_cc_form()

    app.checkout_page.billing.place_order_button.click()


def test_order_pp_popup_bs0(app):

    get(product)

    app.product_page.add_to_cart()
    Wait.visible(app.product_page.minicart_popup_lo)
    app.product_page.minicart_popup.checkout_link.click()

    # *****************************on chechout page

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.checkout_page.fill_shipping_form()

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.checkout_page.fill_billing_form(False)
    app.checkout_page.fill_cc_form()

    app.checkout_page.billing.place_order_button.click()