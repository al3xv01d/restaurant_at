from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from app.app import App
from app.tools import Wait, finds, get
import time
from config import product, server

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


# app.wd.get('https://www.restaurantsupply.com/bloomfield-8543-d2')
# time.sleep(1)
# app.wd.switch_to_frame('livechat-compact-view')
# app.wd.execute_script("document.getElementById('livechat-compact-view').style.display = 'none'")
# app.wd.get('https://www.restaurantsupply.com/winco-c-3080b')

#--------guest - pp
# index -> popup -> checkout -> b=s -> order   --- pass
# index -> popup -> checkout -> b!=s -> order  --- pass
#
# index -> popup -> checkout -> F5 -> b=s -> order    --- pass
# index -> popup -> checkout -> F5 -> b!=s -> order    --- pass
#
# index -> popup -> checkout -> select method -> b=s -> F5 -> b=s -> order   - pass
# index -> popup -> checkout -> select method -> b!=s -> F5 -> b!=s -> order ---pass


#--------guest - pp -
# index -> cart -> checkout -> b=s -> order   --- pass
# index -> cart -> checkout -> b!=s -> order  --- pass
#
# index -> cart -> checkout -> F5 -> b=s -> order -- pass
# index -> cart -> checkout -> F5 -> b!=s -> order
#
# index -> cart -> checkout -> select method -> b=s -> F5 -> b=s -> order
# index -> cart -> checkout -> select method -> b!=s -> F5 -> b!=s -> order


#http://dev.restaurantsupply.com/bloomfield-8543-d2
get('http://gomage777:gomage777@dev.restaurantsupply.com/bloomfield-8543-d2')

app.product_page.add_to_cart()


Wait.visible(app.product_page.minicart_popup_lo)
app.product_page.minicart_popup.view_cart_link.click()

Wait.invisible(app.cart_page.full_page_loader_lo)

# app.cart_page.enter_zip(10001)
#
# Wait.invisible(app.cart_page.full_page_loader_lo)
app.cart_page.checkout_button.click()


# *****************************on chechout page

Wait.invisible(app.cart_page.full_page_loader_lo)

app.checkout_page.fill_shipping_form()

Wait.invisible(app.cart_page.full_page_loader_lo)

#app.checkout_page.fill_billing_form(True)


#app.checkout_page.fill_cc_form()

#app.checkout_page.billing.place_order_button.click()