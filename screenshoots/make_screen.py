from app.screenshoter_config import *
from app.tools import fullpage_screenshot, get, set_site_width
from app.screenshoter_config import browser_catalog
from time import sleep




# MAKE SCREENSHOT - FUNCTIONS

def init_size():
    set_site_width(window_width)


def index_ms():
    get(index)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/0-index.png')

def simple_product_ms():
    get(simple_product)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/1-simple_product.png')

def product_with_related_ms():
    get(product_with_related)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/2-product_with_related.png')

#*********************** DAP ***********************

def dap_on_gesture_ms():
    get(dap_on_gesture)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog +'/3-on_gesture.png')

def dap_in_cart_ms():
    get(dap_in_cart)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog +'/4-in_cart.png')

def dap_before_order_confirmation_ms():
    get(dap_before_order_confirmation)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog +'/5-dap_before_order_confirmation.png')

#************************ CATEGORY TEMPLATES ***********************

def cat_tpl_1_ms():
    get(cat_tpl_1)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/6-cat_tpl_1.png')

def cat_tpl_2_ms():
    get(cat_tpl_2)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/7-cat_tpl_2.png')

def cat_tpl_6_ms():
    get(cat_tpl_6)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/8-cat_tpl_6.png')

def cat_tpl_7_ms():
    get(cat_tpl_7)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/9-cat_tpl_7.png')

def cat_tpl_8_ms():
    get(cat_tpl_8)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/10-cat_tpl_8.png')

def cat_tpl_9_ms():
    get(cat_tpl_9)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/11-cat_tpl_9.png')

def cat_tpl_10_ms():
    get(cat_tpl_10)
    sleep(1)
    fullpage_screenshot(browser_catalog + '/' + resolution_catalog + '/12-cat_tpl_10.png')
