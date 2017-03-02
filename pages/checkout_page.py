from pages.page import Page
from app.tools import find


class ProductPage(Page):

    shipping_email_lo = ''
    shipping_name_lo = ''
    shipping_last_name_lo = ''
    shipping_address_1_lo = ''
    shipping_zip_lo = ''
    shipping_city_lo = ''
    shipping_state_lo = ''
    shipping_country_lo = ''
    shipping_phone_lo = ''
    shipping_next_button = ''


    # --------------------------------  ACTIONS -------------------------------------
    def add_to_cart(self, qty=1):
        if qty > 1:
            self.product_qty.clear()
            self.product_qty.send_keys(qty)
            self.add_to_cart_button.click()
        else:
            self.add_to_cart_button.click()

    def add_related(self, n=1, qty=1):
        if qty > 1:
            self.related_qty(n).clear()
            self.related_qty(n).send_keys(qty)
            self.related_atc_button(n).click()
        else:
            self.related_atc_button(n).click()

    # -------------------------------- RELATED PRODUCT (returns selenium object)-------------------------------------
    def related_product(self, n=1):
        return find(self.related_product_lo % n)

    def related_title(self, n=1):
        return self.related_product(n).find_element_by_xpath(self.related_title_lo)

    def related_qty(self, n=1):
        return self.related_product(n).find_element_by_xpath(self.related_qty_lo)

    def related_atc_button(self,n=1):
        return self.related_product(n).find_element_by_xpath(self.related_product_atc_button_lo)

    @property
    def related_message(self):
        return find(self.related_message_lo)
    # -------------------------------- ELEMENTS (returns selenium object)-------------------------------------
    @property
    def product_qty(self):
        return find(self.product_qty_lo)

    @property
    def add_to_cart_button(self):
        return find(self.add_to_cart_button_lo)

    @property
    def product_title(self):
        return find(self.product_title_lo)
