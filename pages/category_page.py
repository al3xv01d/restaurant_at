from pages.page import Page
from app.tools import find, get


class CategoryPage(Page):

    def __init__(self, n):
        self.product = find("//ol[@class='products list items product-items']/li[%d]" % n)

    def add_to_cart(self, qty=1):
        if qty > 1:
            self.product_qty.clear()
            self.product_qty.send_keys(qty)
            self.add_to_cart_button.click()
        else:
            self.add_to_cart_button.click()
    #--------------------------------  ELEMENTS (returns selenium object) -------------------------------------
    @property
    def product_title(self):
        return self.product.find_element_by_xpath(".//div//strong/a")

    @property
    def product_qty(self):
        return self.product.find_element_by_xpath('.//div//input[@name="qty"]')

    @property
    def add_to_cart_button(self):
        return self.product.find_element_by_xpath('.//button')
