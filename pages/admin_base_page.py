from config import driver, base_url, admin_user, admin_password
from app.tools import find
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AdminBasePage():

    wd = driver

    username_field_lo = '//input[@id="username"]'
    password_field_lo = '//input[@id="login"]'



    # --------------------------------  ACTIONS ------------------------------------------------------------------
    def login(self):
        self.wd.get(base_url + '/restaura_admin/admin/')

        self.username_field.clear()
        self.username_field.send_keys(admin_user + Keys.TAB)
        self.password_field.clear()
        self.password_field.send_keys(admin_password + Keys.RETURN)

    #-------------------------------- COMMON ELEMENTS FOR ALL PAGES (header and footer)-------------------------------------
    @property
    def username_field(self):
        return find(self.username_field_lo)

    @property
    def password_field(self):
        return find(self.password_field_lo)
