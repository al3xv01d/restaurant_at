from config import driver
from app.tools import get, Wait, Random
from config import base_url
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class App:

    wd = driver
    product_page = ProductPage()
    checkout_page = CheckoutPage()
    cart_page = CartPage()

    def __init__(self):
        self.wd.maximize_window()
      #  self.wd.implicitly_wait(60)
       # self.wd.set_page_load_timeout(60)


    def order(self, product, billing_equal_shipping = True):
        get(base_url + product)

        self.product_page.add_to_cart()

        # *****************************on cart page
        Wait.invisible(self.cart_page.full_page_loader_lo)
        self.cart_page.enter_zip(10001)
        Wait.invisible(self.cart_page.full_page_loader_lo)
        self.cart_page.checkout_button.click()

        self.order_fill_order_forms(billing_equal_shipping)
        self.order_fill_cc_form()

        self.checkout_page.place_order_button.click()

    def order_fill_order_forms(self, billing_equal_shipping = True):

        #*********************************SHIPPING PAGE ******************
        Wait.invisible(self.cart_page.full_page_loader_lo)

        self.checkout_page.shipping_email.clear()
        self.checkout_page.shipping_email.send_keys(Random.email())

        self.checkout_page.shipping_name.clear()
        self.checkout_page.shipping_name.send_keys(Random.name())

        self.checkout_page.shipping_company.clear()
        self.checkout_page.shipping_company.send_keys(Random.name())

        self.checkout_page.shipping_last_name.clear()
        self.checkout_page.shipping_last_name.send_keys(Random.name())

        self.checkout_page.shipping_address_1.clear()
        self.checkout_page.shipping_address_1.send_keys(Random.name())

        self.checkout_page.shipping_address_2.clear()
        self.checkout_page.shipping_address_2.send_keys(Random.name())

        self.checkout_page.shipping_zip.clear()
        self.checkout_page.shipping_zip.send_keys(20047)
    
        Wait.visible(self.cart_page.full_page_loader_lo)
        Wait.invisible(self.cart_page.full_page_loader_lo)

        self.checkout_page.shipping_phone.clear()
        self.checkout_page.shipping_phone.send_keys(Random.phone())

        self.checkout_page.next_button.click()
    
        Wait.visible(self.cart_page.full_page_loader_lo)
        Wait.invisible(self.cart_page.full_page_loader_lo)

        #****************************************BILLING PAGE****************************

        self.checkout_page.credit_cart_method.click()

        if billing_equal_shipping:
            Wait.visible(self.checkout_page.billing_equal_shipping_checkbox_lo)
            Wait.invisible(self.checkout_page.full_page_loader_lo)
            self.checkout_page.billing_equal_shipping_checkbox.click()
        else:
            Wait.visible(self.checkout_page.billing_name_lo)

            self.checkout_page.billing_name.clear()
            self.checkout_page.billing_name.send_keys(Random.name())

            self.checkout_page.billing_last_name.clear()
            self.checkout_page.billing_last_name.send_keys(Random.name())

            self.checkout_page.billing_company.clear()
            self.checkout_page.billing_company.send_keys(Random.name())

            self.checkout_page.billing_address_1.clear()
            self.checkout_page.billing_address_1.send_keys(Random.name())

            self.checkout_page.billing_address_2.clear()
            self.checkout_page.billing_address_2.send_keys(Random.name())

            self.checkout_page.billing_zip.clear()
            self.checkout_page.billing_zip.send_keys(20047)

            Wait.visible(self.cart_page.full_page_loader_lo)
            Wait.invisible(self.cart_page.full_page_loader_lo)

            self.checkout_page.billing_phone.clear()
            self.checkout_page.billing_phone.send_keys(Random.phone())

    def order_fill_cc_form(self):
        self.checkout_page.wd.switch_to_frame('braintree-hosted-field-number')
        self.checkout_page.cc_number.send_keys('4111 1111 1111 1111')
        self.wd.switch_to_default_content()

        self.checkout_page.wd.switch_to_frame('braintree-hosted-field-expirationMonth')
        self.checkout_page.cc_month.send_keys(11)
        self.wd.switch_to_default_content()

        self.checkout_page.wd.switch_to_frame('braintree-hosted-field-expirationYear')
        self.checkout_page.cc_year.send_keys(22)
        self.wd.switch_to_default_content()

        self.checkout_page.wd.switch_to_frame('braintree-hosted-field-cvv')
        self.checkout_page.cc_cvv.send_keys(222)
        self.wd.switch_to_default_content()


    def destroy(self):
        self.wd.quit()
