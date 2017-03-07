from pprint import pprint
from app.tools import driver, Wait, Random, fullpage_screenshot
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



#driver.get('https://www.restaurantsupply.com/bloomfield-commercial-coffee-makers-brewers-pourover')
# cat = CategoryPage()
# cat.add_to_cart()
# cp = CartPage()
#
# pprint(cp.item_qty.get_attribute('value'))
# Wait.is_invisible(cp.full_page_loader_lo)



driver.get('https://www.restaurantsupply.com/edlund-11100-old-reliable-1-manual-can-opener-with-plated-steel-base')
pp = ProductPage()
fullpage_screenshot('screenshoots/chrome/1.png')
