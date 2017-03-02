from pprint import pprint
from app.tools import driver, Wait
from pages.product_page import ProductPage
from pages.category_page import CategoryPage
from pages.cart_page import CartPage
from pages.index import IndexPage
from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep



#driver.get('https://www.restaurantsupply.com/bloomfield-commercial-coffee-makers-brewers-pourover')
# cat = CategoryPage()
# cat.add_to_cart()
# cp = CartPage()
#
# pprint(cp.item_qty.get_attribute('value'))
# Wait.is_invisible(cp.full_page_loader_lo)
# cp.empty_cart_link.click()

driver.get('https://www.restaurantsupply.com/bloomfield-8543-d2')
pp = ProductPage()
pp.related_atc_button(2).click()
Wait.visible(pp.cart_counter_number_lo)
pprint(pp.cart_counter_number.text)