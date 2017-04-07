from app.screenshoter_config import *
from config import browser
from app.tools import fullpage_screenshot, get, set_site_width, Wait
from time import sleep
import datetime
import os


class Screenshooter:

    todays_date = str( datetime.date.today() )
    resolution_catalog = ''

    @staticmethod
    def init_size(window_width):
        set_site_width(window_width)
        Screenshooter.resolution_catalog = 'w' + str(window_width)

    @staticmethod
    def generate_folders(): #creating folder for todays_date and for all three resolutions. Folders generates froom ROOT. Root is foldes where test_screenshoot.py located.

        try:
            os.mkdir(browser + '/%s' % Screenshooter.todays_date)
        except:
            pass

        try:
            os.mkdir(browser + '/%s' % Screenshooter.todays_date + '/w1920')
            os.mkdir(browser + '/%s' % Screenshooter.todays_date + '/w1024')
            os.mkdir(browser + '/%s' % Screenshooter.todays_date + '/w768')
        except:
            pass

    # MAKE SCREENSHOTS - different types of pages.
    #Main screenshoot method for simple pages
    @staticmethod
    def make_screenshot(url, file_name=None):
        get(url)
        sleep(1)
        fullpage_screenshot(browser + '/' + Screenshooter.todays_date + '/' + Screenshooter.resolution_catalog + '/' + file_name)


    @staticmethod
    def screen_all(app):
        Screenshooter.make_screenshot(index, '1-index.png')
        Screenshooter.make_screenshot(simple_product, '2-simple-product.png')
        Screenshooter.make_screenshot(product_with_related, '3-product_with_related.png')
        Screenshooter.make_screenshot(product_video, '4-product_video.png')
        Screenshooter.make_screenshot(dap_on_gesture, '5-dap_on_gesture.png')
        Screenshooter.make_screenshot(dap_in_cart, '6-dap_in_cart.png')
        Screenshooter.make_screenshot(dap_before_order_confirmation, '7-dap_before_order_confirmation.png')
        Screenshooter.make_screenshot(cat_tpl_1, '8-cat_tpl_1.png')
        Screenshooter.make_screenshot(cat_tpl_2, '9-cat_tpl_2.png')
        Screenshooter.make_screenshot(cat_tpl_6, '10-cat_tpl_6.png')
        Screenshooter.make_screenshot(cat_tpl_7, '11-cat_tpl_7.png')
        Screenshooter.make_screenshot(cat_tpl_8, '12-cat_tpl_8.png')
        Screenshooter.make_screenshot(cat_tpl_9, '13-cat_tpl_9.png')
        Screenshooter.make_screenshot(cat_tpl_10, '14-cat_tpl_10.png')
        Screenshooter.shipping_page(app)
        Screenshooter.billing_page(app)
        Screenshooter.cart_page(app)

    #Screenshoot methods for pages which needs some interaction

    @staticmethod
    def shipping_page(app):
        get(simple_product)
        app.product_page.add_to_cart()

        Wait.invisible(app.cart_page.full_page_loader_lo)
        Wait.is_clickable(app.cart_page.checkout_button_lo)

        app.cart_page.checkout_button.click()

        Wait.visible(app.cart_page.full_page_loader_lo)
        Wait.invisible(app.cart_page.full_page_loader_lo)

        sleep(0.5)
        fullpage_screenshot(browser + '/' + Screenshooter.todays_date + '/' + Screenshooter.resolution_catalog + '/' + 'shipping-page.png')

    @staticmethod
    def billing_page(app, billing_equal_shipping=False):
        get(simple_product)
        app.product_page.add_to_cart()

        Wait.invisible(app.cart_page.full_page_loader_lo)

        app.cart_page.enter_zip(10001)

        Wait.invisible(app.cart_page.full_page_loader_lo)

        app.cart_page.checkout_button.click()

        Wait.invisible(app.cart_page.full_page_loader_lo)

        app.checkout_page.fill_shipping_form()
        app.checkout_page.billing.credit_cart_method.click()

        Wait.invisible(app.cart_page.full_page_loader_lo)
        sleep(0.5)
        fullpage_screenshot(browser + '/' + Screenshooter.todays_date + '/' + Screenshooter.resolution_catalog + '/' + 'billing-page.png')

    @staticmethod
    def cart_page(app):
        get(product_with_related)

        app.product_page.add_related(1, 2)
        app.product_page.add_related(2, 3)

        app.product_page.add_to_cart()
        Wait.visible(app.cart_page.checkout_button_lo) # for firefox, otherwise don't work
        Wait.invisible(app.cart_page.full_page_loader_lo)
        sleep(0.5)
        fullpage_screenshot(browser + '/' + Screenshooter.todays_date + '/' + Screenshooter.resolution_catalog + '/' + 'cart-page.png')