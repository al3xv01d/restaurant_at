from pages.page import Page
from app.tools import find


class CategoryPage(Page):

    item_lo = '//ol[@class="products list items product-items"]/li[%d]'
    item_title_lo = './/div//strong/a'
    item_qty_lo = './/div//input[@name="qty"]'
    item_atc_button_lo = './/button'

    # --------------------------------  ACTIONS -------------------------------------
    def add_to_cart(self, qty=1, n=1):
        if qty > 1:
            self.item(n).qty.clear()
            self.item(n).qty.send_keys(qty)
            self.item(n).add_to_cart_button.click()
        else:
            self.item(n).add_to_cart_button.click()
    #--------------------------------  PRODUCT IN GRID(n) (returns selenium object) -------------------------------------

    def item(self, n=1):

        class Item():

            def __init__(self, n):
                self.item = find(CategoryPage.item_lo % n)

            @property
            def title(self):
                return self.item.find_element_by_xpath(CategoryPage.item_title_lo)

            @property
            def qty(self):
                return self.item.find_element_by_xpath(CategoryPage.item_qty_lo)

            @property
            def add_to_cart_button(self):
                return self.item.find_element_by_xpath(CategoryPage.item_atc_button_lo)

        return Item(n)