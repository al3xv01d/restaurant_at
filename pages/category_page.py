from pages.page import Page
from app.tools import find, get


class CategoryPage(Page):

    product_lo = '//ol[@class="products list items product-items"]/li[%d]'
    product_title_lo = './/div//strong/a'
    product_qty_lo = './/div//input[@name="qty"]'
    add_to_cart_button_lo = './/button'

    # --------------------------------  ACTIONS -------------------------------------
    def add_to_cart(self, n=1, qty=1):
        if qty > 1:
            self.product_qty(n).clear()
            self.product_qty(n).send_keys(qty)
            self.add_to_cart_button(n).click()
        else:
            self.add_to_cart_button(n).click()
    #--------------------------------  PRODUCT IN GRID(n) (returns selenium object) -------------------------------------

    def product(self, n=1):
        return find(self.product_lo % n)

    def product_title(self, n=1):
        return self.product(n).find_element_by_xpath(self.product_title_lo)

    def product_qty(self, n=1):
        return self.product(n).find_element_by_xpath(self.product_qty_lo)

    def add_to_cart_button(self, n=1):
        return self.product(n).find_element_by_xpath(self.add_to_cart_button_lo)
