from screenshoots.make_screen import *

def screen_all(app):
    index_ms()
    simple_product_ms()
    product_with_related_ms()

    dap_in_cart_ms()
    dap_on_gesture_ms()
    dap_before_order_confirmation_ms()

    cat_tpl_1_ms()
    cat_tpl_2_ms()
    cat_tpl_6_ms()
    cat_tpl_7_ms()
    cat_tpl_8_ms()
    cat_tpl_9_ms()
    cat_tpl_10_ms()

    checkout_page_1_ms(app)

def test_make_screenshots_1920(app):
    init_size(1920)
    screen_all(app)

def test_make_screenshots_1024(app):
    init_size(1024)
    screen_all(app)

def test_make_screenshots_768(app):
    init_size(768)
    screen_all(app)