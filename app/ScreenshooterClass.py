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
    def make_screenshot(url):
        get(url)
        sleep(1)
        fullpage_screenshot(browser + '/' + Screenshooter.todays_date + '/' + Screenshooter.resolution_catalog + '/' + Screenshooter.img_name(url))

    @staticmethod
    def screen_all():
        Screenshooter.make_screenshot(index)
        Screenshooter.make_screenshot(simple_product)
        Screenshooter.make_screenshot(product_with_related)
        Screenshooter.make_screenshot(product_video)
        Screenshooter.make_screenshot(dap_on_gesture)
        Screenshooter.make_screenshot(dap_in_cart)
        Screenshooter.make_screenshot(dap_before_order_confirmation)
        Screenshooter.make_screenshot(cat_tpl_1)
        Screenshooter.make_screenshot(cat_tpl_2)
        Screenshooter.make_screenshot(cat_tpl_6)
        Screenshooter.make_screenshot(cat_tpl_7)
        Screenshooter.make_screenshot(cat_tpl_8)
        Screenshooter.make_screenshot(cat_tpl_9)
        Screenshooter.make_screenshot(cat_tpl_10)
        # Screenshooter.shipping_page(app)
        # Screenshooter.billing_page(app)

    @staticmethod
    def img_name(url):

        if url == base_url + '/':
            return 'index.png'

        if 'san-jamar-s46tbk-46-oz-wall-mounted-bulk-liquid-soap-dispenser-black-pearl' in url:
            return 'simple_product.png'
        if 'bloomfield-8774-a' in url:
            return 'product_with_related_products.png'
        if 'manitowoc-iy-0304a' in url:
            return 'product_with_video.png'

        if '/berkel-mb-3-8' in url:
            return 'dap_on_gesture.png'
        if '/amana-rfs18ts-medium-duty-stainless-steel-commercial-microwave-with-push-button-controls-208-230v-1800w' in url:
            return 'dap_in_cart.png'
        if '/manitowoc-jc-0995' in url:
            return 'dap_before_order_confirmation.png'

        if '/best-sellers' in url:
            return 'category_template_1.png'
        if '/storage-and-transport' in url:
            return 'category_template_2.png'
        if '/food-preparation' in url:
            return 'category_template_6.png'
        if '/everpure' in url:
            return 'category_template_7.png'
        if '/best-selling-fryer-baskets' in url:
            return 'category_template_8.png'
        if '/janitorial-supplies' in url:
            return 'category_template_9.png'
        if '/table-mounted-stainless-steel-shelving-units' in url:
            return 'category_template_10.png'

    #Screenshoot methods for pages which needs some interaction

    @staticmethod
    def shipping_page(app):
        get(simple_product)
        app.product_page.add_to_cart()

        Wait.invisible(app.cart_page.full_page_loader_lo)
        Wait.is_clickable(app.cart_page.checkout_button_lo)

        app.cart_page.checkout_button.click()
        sleep(2)
        fullpage_screenshot(browser + '/' + Screenshooter.todays_date + '/' + Screenshooter.resolution_catalog + '/' + 'shipping-page.png')

    @staticmethod
    def billing_page(app, billing_equal_shipping=False):
        get(simple_product)
        app.product_page.add_to_cart()

        Wait.visible(app.cart_page.full_page_loader_lo)
        Wait.invisible(app.cart_page.full_page_loader_lo)

        # app.cart_page.enter_zip(10001)

        Wait.invisible(app.cart_page.full_page_loader_lo)

        app.cart_page.checkout_button.click()

        Wait.invisible(app.cart_page.full_page_loader_lo)

        app.checkout_page.fill_order_forms(billing_equal_shipping)

        fullpage_screenshot(browser + '/' + Screenshooter.todays_date + '/' + Screenshooter.resolution_catalog + '/' + 'shipping-page.png')