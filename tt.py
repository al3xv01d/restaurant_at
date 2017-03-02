from pprint import pprint
from app.tools import driver, Wait, Random
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


driver.get('https://www.restaurantsupply.com/bloomfield-8543-d2')
pp = ProductPage()
cp = CartPage()
pp.add_to_cart()
sp = CheckoutPage()
Wait.invisible(cp.full_page_loader_lo)

cp.enter_zip(10001)
Wait.invisible(cp.full_page_loader_lo)
cp.checkout_button.click()
Wait.invisible(cp.full_page_loader_lo)
##############################################SHIPPING
sp.shipping_email.clear()
sp.shipping_email.send_keys(Random.email())

sp.shipping_name.clear()
sp.shipping_name.send_keys(Random.name())

sp.shipping_company.clear()
sp.shipping_company.send_keys(Random.name())

sp.shipping_last_name.clear()
sp.shipping_last_name.send_keys(Random.name())

sp.shipping_address_1.clear()
sp.shipping_address_1.send_keys(Random.name())

sp.shipping_address_2.clear()
sp.shipping_address_2.send_keys(Random.name())

sp.shipping_zip.clear()
sp.shipping_zip.send_keys(20047)

Wait.visible(cp.full_page_loader_lo)
Wait.invisible(cp.full_page_loader_lo)

sp.shipping_phone.clear()
sp.shipping_phone.send_keys(Random.phone())

sp.next_button.click()

Wait.visible(cp.full_page_loader_lo)
Wait.invisible(cp.full_page_loader_lo)
################################################BILING
sp.credit_cart_method.click()

Wait.visible(sp.billing_equal_shipping_checkbox_lo)
Wait.invisible(cp.full_page_loader_lo)
sp.billing_equal_shipping_checkbox.click()


# Wait.visible(sp.cc_number)




sp.place_order_button.click()