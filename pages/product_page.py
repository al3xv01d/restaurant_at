from pages.page import Page
from app.tools import find, get


class ProductPage(Page):

    product_qty_lo = '//input[@id="qty"]'
    add_to_cart_button_lo = '//button[@id="product-addtocart-button"]'
    product_title_lo = '//span[@data-ui-id="page-title-wrapper"]'

    # --------------------------------  ACTIONS -------------------------------------
    def add_to_cart(self, qty=1):
        if qty > 1:
            self.product_qty.clear()
            self.product_qty.send_keys(qty)
            self.add_to_cart_button.click()
        else:
            self.add_to_cart_button.click()

    #-------------------------------- COMMON LOCATORS (header and footer)-------------------------------------
    @property
    def product_qty(self):
        return find(self.product_qty_lo)

    @property
    def add_to_cart_button(self):
        return find(self.add_to_cart_button_lo)

    @property
    def product_title(self):
        return find(self.product_title_lo)
