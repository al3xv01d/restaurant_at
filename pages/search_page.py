from pages.page import Page
from app.tools import find


class SearchPage(Page):

    item_lo = '//ul[@class="products-grid row"]/li[%d]'
    item_qty_lo = './/input[@name="qty"]'
    item_title_lo = './/div[@class="product-shop"]//a'
    item_atc_button_lo = './/button'


    # --------------------------------  ACTIONS ------------------------------------------------------------------

    def add_to_cart(self, qty=1, n=1):
        if qty > 1:
            self.item(n).qty.clear()
            self.item(n).qty.send_keys(qty)
            self.item(n).atc_button.click()
        else:
            self.item(n).atc_button.click()

    #-------------------------------- ITEM ELEMENTS (returns selenium object)-------------------------------------
    #product item in cart
    def item(self, n=1):

        class Item():

            def __init__(self, n):
                self.item = find(SearchPage.item_lo % n)

            @property
            def qty(self):
                return self.item.find_element_by_xpath(SearchPage.item_qty_lo)

            @property
            def title(self):
                return self.item.find_element_by_xpath(SearchPage.item_title_lo)

            @property
            def atc_button(self):
                return self.item.find_element_by_xpath(SearchPage.item_atc_button_lo)

        return Item(n)

    # -------------------------------- ELEMENTS (returns selenium object)-------------------------------------





