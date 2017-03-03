from pages.page import Page
from app.tools import find


class SearchPage(Page):

    item_lo = '//ul[@class="products-grid row"]/li[%d]'
    item_qty_lo = './/input[@name="qty"]'
    item_title_lo = './/div[@class="product-shop"]//a'
    item_atc_button_lo = './/button'


    # --------------------------------  ACTIONS ------------------------------------------------------------------

    def add_to_cart(self, n=1, qty=1):
        if qty > 1:
            self.item_qty(n).clear()
            self.item_qty(n).send_keys(qty)
            self.item_atc_button(n).click()
        else:
            self.item_atc_button(n).click()

    #-------------------------------- ITEM ELEMENTS (returns selenium object)-------------------------------------
    #product item in cart
    def item(self, n=1):
        return find(self.item_lo % n)

    def item_qty(self, n=1):
        return self.item(n).find_element_by_xpath(self.item_qty_lo)

    def item_title(self, n=1):
        return self.item(n).find_element_by_xpath(self.item_title_lo)

    def item_atc_button(self, n=1):
        return self.item(n).find_element_by_xpath(self.item_atc_button_lo)

    # -------------------------------- ELEMENTS (returns selenium object)-------------------------------------





