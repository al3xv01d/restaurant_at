from pages.page import Page
from app.tools import find, Wait


class ProductPage(Page):

    product_qty_lo = '//input[@id="qty"]'
    add_to_cart_button_lo = '//button[@id="product-addtocart-button"]'
    product_title_lo = '//span[@data-ui-id="page-title-wrapper"]'
    product_img_lo = '//img[@class="fotorama__img"]'

    related_lo = '//div[@class="b-fbt-products"]/li[%d]'
    related_atc_button_lo = './/button'
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
            self.related(n).qty.clear()
            self.related(n).qty.send_keys(qty)
            self.related(n).atc_button.click()
        else:
            self.related(n).atc_button.click()

    # -------------------------------- RELATED PRODUCT (returns selenium object)-------------------------------------
    def related(self, n=1):

        class Related:

            def __init__(self, n):
                self.related = find(ProductPage.related_lo % n)

            @property
            def title(self):
                return self.related.find_element_by_xpath(ProductPage.related_title_lo)

            @property
            def qty(self):
                return self.related.find_element_by_xpath(ProductPage.related_qty_lo)

            @property
            def atc_button(self):
                return self.related.find_element_by_xpath(ProductPage.related_atc_button_lo)

        return Related(n)

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
