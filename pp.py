from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from app.app import App
from app.tools import Wait
import time

app = App()
#
# desired_cap = {'browser': 'Safari', 'browser_version': '10.0', 'os': 'OS X', 'os_version': 'Sierra', 'resolution': '1920x1080'}
# app.wd = webdriver.Remote(
#     command_executor='http://vadymantsyferov1:smT8fwsFdxEBsi7bUWcd@hub.browserstack.com:80/wd/hub',
#     desired_capabilities=desired_cap)
#
# app.wd.get('https://restaurantsupply.com/bloomfield-8543-d2')
#
# app.product_page.add_to_cart()
# app.cart_page.enter_zip(20000)
#
# app.wd.quit()


app.wd.get('https://www.restaurantsupply.com/bloomfield-8543-d2')

# app.screenshooter.cart_page(app)

app.product_page.add_related(1,2)
app.product_page.add_related(2,3)

app.product_page.add_to_cart()