from pprint import pprint
from app.tools import  Wait, get, find, Random, fullpage_screenshot, set_site_width
from config import driver
from pages.product_page import ProductPage
from pages.category_page import CategoryPage
from pages.cart_page import CartPage
from pages.index import IndexPage
from pages.page import Page
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import pp
from app import screenshoter_config
from screenshoots.make_screen import *



get('http://dev.restaurantsupply.com/restaura_admin/admin')

login = find(".//*[@id='username']")
password = find(".//*[@id='login']")

login.clear()
login.send_keys('akh')

password.clear()
password.send_keys('34-gtshKF5sgD2')

find('//*[@id="login-form"]/fieldset/div[3]/div[1]/button/span').click()

products = find(".//*[@id='menu-magento-catalog-catalog']/a")
products.click()

#catalog link
find(".//*[@id='menu-magento-catalog-catalog']/div/ul/li/div/ul/li[1]/a/span").click()