from pages.page import Page
from app.tools import find, get


class ProductPage(Page):

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
        return find('//input[@id="qty"]')

    @property
    def add_to_cart_button(self):
        return find('//button[@id="product-addtocart-button"]')

    @property
    def product_title(self):
        return find('//span[@data-ui-id="page-title-wrapper"]')
