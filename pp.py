from pages.product_page import ProductPage
from app.tools import get, find
from config import base_url
from pprint import pprint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


get(base_url + '/bloomfield-8774-a')
pp = ProductPage()
qty = 11
pp.add_to_cart(qty)

#WebDriverWait(pp.wd, 10).until(EC.staleness_of(pp.add_to_cart_button))

cart_qty = int(find('//input[@title="Qty"]').get_attribute('value'))


print(cart_qty)

assert cart_qty == qty



