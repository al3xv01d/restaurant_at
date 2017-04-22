from config import driver
from app.tools import get, Wait, Random
from config import base_url, product
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.category_page import CategoryPage
from pages.index import IndexPage
from pages.search_page import SearchPage
from app.ScreenshooterClass import Screenshooter

from time import sleep

class App:

    wd = driver
    product_page = ProductPage()
    checkout_page = CheckoutPage()
    cart_page = CartPage()
    category_page = CategoryPage()
    index_page = IndexPage()
    search_page = SearchPage()
    screenshooter = Screenshooter()

    def __init__(self):
        self.wd.maximize_window()
      #  self.wd.implicitly_wait(60)
       # self.wd.set_page_load_timeout(60)


    def order(self, billing_equal_shipping = True):
        get(product)

        self.product_page.add_to_cart()
        Wait.visible(self.product_page.minicart_popup_lo)
        self.product_page.minicart_popup.view_cart_link.click()

        # *****************************on cart page
        Wait.invisible(self.cart_page.full_page_loader_lo)

        self.cart_page.enter_zip(10001)

        Wait.invisible(self.cart_page.full_page_loader_lo)

        self.cart_page.checkout_button.click()

        Wait.invisible(self.cart_page.full_page_loader_lo)

        self.checkout_page.fill_shipping_form()

        Wait.invisible(self.cart_page.full_page_loader_lo)
        #sleep(5)
        self.checkout_page.fill_billing_form(billing_equal_shipping)
        self.checkout_page.fill_cc_form()

        self.checkout_page.billing.place_order_button.click()


    def destroy(self):
        self.wd.quit()
