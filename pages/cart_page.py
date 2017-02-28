from pages.page import Page
from app.tools import find


class CartPage(Page):

    empty_cart_link_lo = '//button[@id="empty_cart_button"]'
    checkout_button_lo = '//input[@id="qty"]'
    zip_code_field_lo = '//input[@id="IX1UU3A"]'
    #item locators
    item_qty_lo = './/input[@title="Qty"]'
    item_title_lo = './/strong[@class="product-item-name"]/a'


    # --------------------------------  ACTIONS ------------------------------------------------------------------
    def enter_zip(self, zip):
        self.zip_code_field.clear()
        self.zip_code_field.send_keys(zip)


    #-------------------------------- ITEM ELEMENTS (returns selenium object)-------------------------------------
   #product item in cart
    def item(self, n=1):
        return find('//table[@id="shopping-cart-table"]/tbody/tr[%d]' % n)

    @property
    def item_qty(self):
        return self.item().find_element_by_xpath(self.item_qty_lo)

    @property
    def item_title(self):
        return self.item().find_element_by_xpath(self.item_title_lo)

    # -------------------------------- ELEMENTS (returns selenium object)-------------------------------------
    @property
    def empty_cart_link(self):
        return find(self.empty_cart_link_lo)

    @property
    def checkout_button(self):
        return find(self.checkout_button_lo)

    @property
    def zip_code_field(self):
        return find(self.zip_code_field_lo)




