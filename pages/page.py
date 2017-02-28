from config import driver, user, password
from app.tools import find
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Page():

    wd = driver

    login_icon_lo = '//ul[@class="header-links"]/li[4]'
    logout_link_lo = '//a[contains(@href, "customer/account/logout/")]'
    cart_counter_lo = '//span[@class="counter-number"]'
    search_input_lo = '//input[@id="search"]'
    search_button_lo = '//button[@id="search_button"]'

    # --------------------------------  ACTIONS ------------------------------------------------------------------
    def login(self):
        self.login_icon.click()

        login_email = find('//input[@id="login-email"]')
        login_password = find('//input[@id="login-password"]')

        login_email.clear()
        login_email.send_keys(user + Keys.TAB)
        login_password.clear()
        login_password.send_keys(password + Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.staleness_of(self.login_icon))

    def logout(self):

        self.login_icon.click()
        self.logout_link.click()

    def find(self, search_term):
        self.search_input.clear()
        self.search_input.send_keys(search_term)
        self.search_button.click()

    #-------------------------------- COMMON FOR ALL PAGES ELEMENTS (header and footer)-------------------------------------
    @property
    def login_icon(self):
        return find(self.login_icon_lo)

    @property
    def logout_link(self):
        return find(self.logout_link_lo)

    @property
    def cart_counter(self):
        return find(self.cart_counter_lo)

    @property
    def search_input(self):
        return find(self.search_input_lo)

    @property
    def search_button(self):
        return find(self.search_button_lo)

