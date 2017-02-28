from config import driver, user, password
from app.tools import find
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Page():

    wd = driver

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



    #-------------------------------- COMMON LOCATORS (header and footer)-------------------------------------
    @property
    def login_icon(self):
        return find('//ul[@class="header-links"]/li[4]')

    @property
    def logout_link(self):
        return find('//a[contains(@href, "customer/account/logout/")]')

    @property
    def cart_counter(self):
        return find('//span[@class="counter-number"]')

