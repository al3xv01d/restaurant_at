from app.tools import get, Wait, finds
from config import product


def test_invalid_zip_on_shipping_page(app):
    get(product)
    app.product_page.add_to_cart()
    Wait.visible(app.product_page.minicart_popup_lo)
    app.product_page.minicart_popup.view_cart_link.click()

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.cart_page.enter_zip('06001')

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.cart_page.checkout_button.click()

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.checkout_page.shipping.zip.clear()
    app.checkout_page.shipping.zip.send_keys('06001')

    Wait.visible(app.cart_page.full_page_loader_lo)
    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.checkout_page.shipping.zip.clear()
    app.checkout_page.shipping.zip.send_keys('55555')

    errors_text_array = finds('//div[@class="mage-error"]')

    assert errors_text_array[0].text == 'This is a required field.'
    assert errors_text_array[1].text == 'This is a required field.'
