from pprint import pprint
from app.tools import driver, Wait
from pages.product_page import ProductPage
from pages.category_page import CategoryPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep



driver.get('https://www.restaurantsupply.com/bloomfield-commercial-coffee-makers-brewers-pourover')
cp = CategoryPage(2)
title = cp.product_title.text
cp.product_qty.send_keys(1)
# product = driver.find_element_by_xpath("//ol[@class='products list items product-items']/li[9]")
# title = product.find_element_by_xpath(".//div//strong/a").text
pprint(title)

cp.add_to_cart_button.click()
#driver.quit()
#
# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//button[@id="empty_cart_button"]'))
# )

