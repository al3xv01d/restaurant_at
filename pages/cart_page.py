from pages.page import Page
from app.tools import find, get


class CartPage(Page):

    def enter_zip(self, zip):
        self.zip_code_field.clear()
        self.zip_code_field.send_keys(zip)


    #-------------------------------- COMMON Elements (header and footer)-------------------------------------
    @property
    def empty_cart_link(self):
        return find('//button[@id="empty_cart_button"]')

    @property
    def checkout_button(self):
        return find('//input[@id="qty"]')

    @property
    def zip_code_field(self):
        return find('//input[@id="IX1UU3A"]')




# //input[@title='Qty']   - qty in cart