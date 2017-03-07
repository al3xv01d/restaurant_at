from app.tools import Wait


def test_order_with_invalid_cc(app):

    app.order()

    Wait.visible(app.checkout_page.error_message_lo)

    assert 'Something Went Wrong. Please call 855-838-1010.' in app.checkout_page.error_message.text






