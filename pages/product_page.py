from pages.page import Page
from app.tools import find, Wait


class ProductPage(Page):

    product_qty_lo = '//input[@id="qty"]'
    add_to_cart_button_lo = '//button[@id="product-addtocart-button"]'
    product_title_lo = '//span[@data-ui-id="page-title-wrapper"]'
    product_img_lo = '//img[@class="fotorama__img"]'

    related_product_lo = '//div[@class="b-fbt-products"]/li[%d]'
    related_product_atc_button_lo = './/button'
    related_title_lo = './/strong/a'
    related_qty_lo = './/input[@name="qty"]'

    related_message_lo = '//div[@data-placeholder="messages"]'
    related_modal_lo = '//div[@class="customization_add_cart_new_product"]//span[2]'

    # --------------------------------  ACTIONS -------------------------------------
    def add_to_cart(self, qty=1):
        Wait.visible(self.product_img_lo)
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

    @property
    def related_modal(self):
        return find(self.related_modal_lo)

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
