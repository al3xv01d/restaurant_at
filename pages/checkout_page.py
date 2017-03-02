from pages.page import Page
from app.tools import find


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


    # --------------------------------  ACTIONS -------------------------------------
    def add_to_cart(self, qty=1):
        pass


    # -------------------------------- SHIPPING PAGE ELEMENTS (returns selenium object)-------------------------------------
    @property
    def shipping_email(self):
        return find(self.shipping_email_lo)

    @property
    def shipping_name(self):
        return find(self.shipping_name_lo)

    @property
    def shipping_last_name(self):
        return find(self.shipping_last_name_lo)

    @property
    def shipping_company(self):
        return find(self.shipping_company_lo)

    @property
    def shipping_address_1(self):
        return find(self.shipping_address_1_lo)

    @property
    def shipping_address_2(self):
        return find(self.shipping_address_2_lo)

    @property
    def shipping_zip(self):
        return find(self.shipping_zip_lo)

    @property
    def shipping_city(self):
        return find(self.shipping_city_lo)

    @property
    def shipping_state(self):
        return find(self.shipping_state_lo)

    @property
    def shipping_country(self):
        return find(self.shipping_country_lo)

    @property
    def shipping_phone(self):
        return find(self.shipping_phone_lo)

    @property
    def next_button(self):
        return find(self.next_button_lo)

    # -------------------------------- BILLING PAGE ELEMENTS (returns selenium object)-------------------------------------
    @property
    def credit_cart_method(self):
        return find(self.credit_cart_method_lo)

    @property
    def billing_equal_shipping_checkbox(self):
        return find(self.billing_equal_shipping_checkbox_lo)

    @property
    def billing_name(self):
        return find(self.billing_name_lo)

    @property
    def billing_last_name(self):
        return find(self.billing_last_name_lo)

    @property
    def billing_company(self):
        return find(self.billing_company_lo)

    @property
    def billing_address_1(self):
        return find(self.billing_address_1_lo)

    @property
    def billing_address_2(self):
        return find(self.billing_address_2_lo)

    @property
    def billing_zip(self):
        return find(self.billing_zip_lo)

    @property
    def billing_city(self):
        return find(self.billing_city_lo)

    @property
    def billing_state(self):
        return find(self.billing_state_lo)

    @property
    def billing_country(self):
        return find(self.billing_country_lo)

    @property
    def billing_phone(self):
        return find(self.billing_phone_lo)

    #****************CREDIT CART FORM

    @property
    def cc_number(self):
        return find(self.cc_number_lo)

    @property
    def cc_month(self):
        return find(self.cc_month_lo)

    @property
    def cc_year(self):
        return find(self.cc_year_lo)

    @property
    def cc_cvv(self):
        return find(self.cc_cvv_lo)

    # place order button
    @property
    def place_order_button(self):
        return find(self.place_order_button_lo)