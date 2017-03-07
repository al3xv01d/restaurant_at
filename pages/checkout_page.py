from pages.page import Page
from app.tools import find, Random, Wait


class CheckoutPage(Page):
    # **************************SHIPPING PAGE LOCATORS ******************************
    shipping_email_lo = '//input[@id="customer-email"]'

    shipping_name_lo = '//form[@id="co-shipping-form"]//input[@name="firstname"]'
    shipping_last_name_lo = '//form[@id="co-shipping-form"]//input[@name="lastname"]'
    shipping_company_lo = '//form[@id="co-shipping-form"]//input[@name="company"]'
    shipping_address_1_lo = '//form[@id="co-shipping-form"]//input[@name="street[0]"]'
    shipping_address_2_lo = '//form[@id="co-shipping-form"]//input[@name="street[1]"]'
    shipping_zip_lo = '//form[@id="co-shipping-form"]//input[@name="postcode"]'
    shipping_city_lo = '//form[@id="co-shipping-form"]//input[@name="city"]'
    shipping_state_lo = '//form[@id="co-shipping-form"]//select[@name="region_id"]'
    shipping_country_lo = '//form[@id="co-shipping-form"]//select[@name="country_id"]'
    shipping_phone_lo = '//form[@id="co-shipping-form"]//input[@name="telephone"]'

    next_button_lo = '//button[@data-role="opc-continue"]'

    #**************************BILLING PAGE LOCATORS ******************************
    credit_cart_method_lo = '//div[@class="payment-method-title field choice"][1]//span'
    billing_equal_shipping_checkbox_lo = '//input[@id="billing-address-same-as-shipping-braintree"]'

    billing_name_lo ='//form[@id="co-payment-form"]//input[@name="firstname"]'
    billing_last_name_lo = '//form[@id="co-payment-form"]//input[@name="lastname"]'
    billing_company_lo = '//form[@id="co-payment-form"]//input[@name="company"]'
    billing_address_1_lo = '//form[@id="co-payment-form"]//input[@name="street[0]"]'
    billing_address_2_lo = '//form[@id="co-payment-form"]//input[@name="street[1]"]'
    billing_zip_lo = '//form[@id="co-payment-form"]//input[@name="postcode"]'
    billing_city_lo = '//form[@id="co-payment-form"]//input[@name="city"]'
    billing_state_lo = '//form[@id="co-payment-form"]//select[@name="region_id"]'
    billing_country_lo = '//form[@id="co-payment-form"]//select[@name="country_id"]'
    billing_phone_lo = '//form[@id="co-payment-form"]//input[@name="telephone"]'

    cc_number_lo = '//input[@id="credit-card-number"]'
    cc_month_lo = '//input[@id="expiration-month"]'
    cc_year_lo = '//input[@id="expiration-year"]'
    cc_cvv_lo = '//input[@id="cvv"]'

    place_order_button_lo = '//div[@id="checkout-payment-method-load"]//div[@class="actions-toolbar"]//div[@class="primary"]//button[@title="Place Order"]'

    error_message_lo = '//div[@data-ui-id="checkout-cart-validationmessages-message-error"]'

    @property
    def error_message(self):
        return find(self.error_message_lo)

    # --------------------------------  ACTIONS -------------------------------------

    def fill_order_forms(self, billing_equal_shipping=True):

        #*********************************SHIPPING PAGE ******************

        self.shipping.email.clear()
        self.shipping.email.send_keys(Random.email())

        self.shipping.name.clear()
        self.shipping.name.send_keys(Random.name())

        self.shipping.company.clear()
        self.shipping.company.send_keys(Random.name())

        self.shipping.last_name.clear()
        self.shipping.last_name.send_keys(Random.name())

        self.shipping.address_1.clear()
        self.shipping.address_1.send_keys(Random.name())

        self.shipping.address_2.clear()
        self.shipping.address_2.send_keys(Random.name())

        self.shipping.zip.clear()
        self.shipping.zip.send_keys(20047)

        Wait.visible(self.full_page_loader_lo)
        Wait.invisible(self.full_page_loader_lo)

        self.shipping.phone.clear()
        self.shipping.phone.send_keys(Random.phone())

        self.shipping.next_button.click()

        Wait.visible(self.full_page_loader_lo)
        Wait.invisible(self.full_page_loader_lo)

        #****************************************BILLING PAGE****************************

        self.billing.credit_cart_method.click()

        if billing_equal_shipping:
            Wait.visible(self.billing_equal_shipping_checkbox_lo)
            Wait.invisible(self.full_page_loader_lo)
            self.billing.billing_equal_shipping_checkbox.click()
        else:
            Wait.visible(self.billing_name_lo)

            self.billing.name.clear()
            self.billing.name.send_keys(Random.name())

            self.billing.last_name.clear()
            self.billing.last_name.send_keys(Random.name())

            self.billing.company.clear()
            self.billing.company.send_keys(Random.name())

            self.billing.address_1.clear()
            self.billing.address_1.send_keys(Random.name())

            self.billing.address_2.clear()
            self.billing.address_2.send_keys(Random.name())

            self.billing.zip.clear()
            self.billing.zip.send_keys(20047)

            Wait.visible(self.full_page_loader_lo)
            Wait.invisible(self.full_page_loader_lo)

            self.billing.phone.clear()
            self.billing.phone.send_keys(Random.phone())

    def fill_cc_form(self):
        self.wd.switch_to_frame('braintree-hosted-field-number')
        self.billing.cc_number.send_keys('4111 1111 1111 1111')
        self.wd.switch_to_default_content()

        self.wd.switch_to_frame('braintree-hosted-field-expirationMonth')
        self.billing.cc_month.send_keys(11)
        self.wd.switch_to_default_content()

        self.wd.switch_to_frame('braintree-hosted-field-expirationYear')
        self.billing.cc_year.send_keys(22)
        self.wd.switch_to_default_content()

        self.wd.switch_to_frame('braintree-hosted-field-cvv')
        self.billing.cc_cvv.send_keys(222)
        self.wd.switch_to_default_content()

    # -------------------------------- SHIPPING PAGE ELEMENTS (returns selenium object)-------------------------------------
    @property
    def shipping(self):

        class Shipping:

            @property
            def email(self):
                return find(CheckoutPage.shipping_email_lo)

            @property
            def name(self):
                return find(CheckoutPage.shipping_name_lo)

            @property
            def last_name(self):
                return find(CheckoutPage.shipping_last_name_lo)

            @property
            def company(self):
                return find(CheckoutPage.shipping_company_lo)

            @property
            def address_1(self):
                return find(CheckoutPage.shipping_address_1_lo)

            @property
            def address_2(self):
                return find(CheckoutPage.shipping_address_2_lo)

            @property
            def zip(self):
                return find(CheckoutPage.shipping_zip_lo)

            @property
            def city(self):
                return find(CheckoutPage.shipping_city_lo)

            @property
            def state(self):
                return find(CheckoutPage.shipping_state_lo)

            @property
            def country(self):
                return find(CheckoutPage.shipping_country_lo)

            @property
            def phone(self):
                return find(CheckoutPage.shipping_phone_lo)

            @property
            def next_button(self):
                return find(CheckoutPage.next_button_lo)

        return Shipping()

    # -------------------------------- BILLING PAGE ELEMENTS (returns selenium object)-------------------------------------
    @property
    def billing(self):

        class Billing:

            @property
            def credit_cart_method(self):
                return find(CheckoutPage.credit_cart_method_lo)

            @property
            def billing_equal_shipping_checkbox(self):
                return find(CheckoutPage.billing_equal_shipping_checkbox_lo)

            @property
            def name(self):
                return find(CheckoutPage.billing_name_lo)

            @property
            def last_name(self):
                return find(CheckoutPage.billing_last_name_lo)

            @property
            def company(self):
                return find(CheckoutPage.billing_company_lo)

            @property
            def address_1(self):
                return find(CheckoutPage.billing_address_1_lo)

            @property
            def address_2(self):
                return find(CheckoutPage.billing_address_2_lo)

            @property
            def zip(self):
                return find(CheckoutPage.billing_zip_lo)

            @property
            def city(self):
                return find(CheckoutPage.billing_city_lo)

            @property
            def state(self):
                return find(CheckoutPage.billing_state_lo)

            @property
            def country(self):
                return find(CheckoutPage.billing_country_lo)

            @property
            def phone(self):
                return find(CheckoutPage.billing_phone_lo)

            #****************CREDIT CART FORM**************************

            @property
            def cc_number(self):
                return find(CheckoutPage.cc_number_lo)

            @property
            def cc_month(self):
                return find(CheckoutPage.cc_month_lo)

            @property
            def cc_year(self):
                return find(CheckoutPage.cc_year_lo)

            @property
            def cc_cvv(self):
                return find(CheckoutPage.cc_cvv_lo)

            # place order button
            @property
            def place_order_button(self):
                return find(CheckoutPage.place_order_button_lo)

        return Billing()