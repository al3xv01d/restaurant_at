from pages.page import Page
from app.tools import find


class CartPage(Page):

    empty_cart_link_lo = '//button[@id="empty_cart_button"]'
    zip_code_field_lo = '//input[@name="postcode"]'
    checkout_button_lo = '//button[@data-role="proceed-to-checkout"]'

    #item locators
    item_lo = '//table[@id="shopping-cart-table"]/tbody/tr[%d]'
    item_qty_lo = './/input[@title="Qty"]'
    item_title_lo = './/strong[@class="product-item-name"]/a'
    item_price_lo = './td[@data-th="Subtotal"]//span[@class="price"]'

    tax_price_lo = '//tr[@class="totals-tax"]/td/span'


    # --------------------------------  ACTIONS ------------------------------------------------------------------
    def enter_zip(self, zip):
        self.zip_code_field.clear()
        self.zip_code_field.send_keys(zip)


    #-------------------------------- ITEM ELEMENTS (returns selenium object)-------------------------------------
    def item(self, n=1):

        class Item:

            def __init__(self, n):
                self.item = find(CartPage.item_lo % n)

            @property
            def title(self):
                return self.item.find_element_by_xpath(CartPage.item_title_lo)

            @property
            def qty(self):
                return self.item.find_element_by_xpath(CartPage.item_qty_lo)

            @property
            def price(self):
                return self.item.find_element_by_xpath(CartPage.item_price_lo)

        return Item(n)

    # -------------------------------- ELEMENTS (returns selenium object)-------------------------------------
    @property
    def empty_cart_link(self):
        return find(self.empty_cart_link_lo)

    @property
    def zip_code_field(self):
        return find(self.zip_code_field_lo)

    @property
    def checkout_button(self):
        return find(self.checkout_button_lo)

    @property
    def tax_price(self):
        return find(self.tax_price_lo)





