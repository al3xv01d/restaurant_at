from app.screenshoter_config import *
from config import browser
from app.tools import fullpage_screenshot, get, set_site_width,Wait
from time import sleep
import datetime
import os

todays_date = datetime.date.today()

def make_folder_for_todays_date():
    try:
        os.mkdir(browser + '/%s' % todays_date)
    except:
        pass
    
    try:
        os.mkdir(browser + '/%s' % todays_date + '/w1920')
        os.mkdir(browser + '/%s' % todays_date + '/w1024')
        os.mkdir(browser + '/%s' % todays_date + '/w768')
    except:
        pass

    

resolution_catalog = ''

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


# MAKE SCREENSHOT - FUNCTIONS

def init_size(window_width):
    set_site_width(window_width)
    global resolution_catalog
    resolution_catalog = 'w' + str(window_width)

def index_ms():
    get(index)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/0-index.png')

def simple_product_ms():
    get(simple_product)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/1-simple_product.png')

def product_with_related_ms():
    get(product_with_related)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/2-product_with_related.png')

#*********************** Display Actual Price ***********************

def dap_on_gesture_ms():
    get(dap_on_gesture)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog +'/3-on_gesture.png')

def dap_in_cart_ms():
    get(dap_in_cart)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog +'/4-in_cart.png')

def dap_before_order_confirmation_ms():
    get(dap_before_order_confirmation)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog +'/5-dap_before_order_confirmation.png')

#************************ CATEGORY TEMPLATES ***********************

def cat_tpl_1_ms():
    get(cat_tpl_1)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/6-cat_tpl_1.png')

def cat_tpl_2_ms():
    get(cat_tpl_2)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/7-cat_tpl_2.png')

def cat_tpl_6_ms():
    get(cat_tpl_6)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/8-cat_tpl_6.png')

def cat_tpl_7_ms():
    get(cat_tpl_7)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/9-cat_tpl_7.png')

def cat_tpl_8_ms():
    get(cat_tpl_8)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/10-cat_tpl_8.png')

def cat_tpl_9_ms():
    get(cat_tpl_9)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/11-cat_tpl_9.png')

def cat_tpl_10_ms():
    get(cat_tpl_10)
    sleep(1)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/12-cat_tpl_10.png')

def cart_page_ms(app):
    get(simple_product)
    app.product_page.add_to_cart()
    sleep(5)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/13-cart_page.png')

def checkout_page_1_ms(app):
    get(simple_product)
    app.product_page.add_to_cart()
    Wait.invisible(app.cart_page.full_page_loader_lo)
    Wait.is_clickable(app.cart_page.checkout_button_lo)
    app.cart_page.checkout_button.click()
    sleep(2)
    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/14-checkout_page_1.png')

def checkout_page_2_ms(app, billing_equal_shipping=False):
    get(simple_product)
    app.product_page.add_to_cart()

    Wait.visible(app.cart_page.full_page_loader_lo)
    Wait.invisible(app.cart_page.full_page_loader_lo)

    #app.cart_page.enter_zip(10001)

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.cart_page.checkout_button.click()

    Wait.invisible(app.cart_page.full_page_loader_lo)

    app.checkout_page.fill_order_forms(billing_equal_shipping)

    fullpage_screenshot(browser + '/' + '/' + str(todays_date) + '/' + resolution_catalog + '/15-billing_page.png')