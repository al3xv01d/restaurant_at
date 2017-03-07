from app.tools import get, fullpage_screenshot
from config import driver, browser
from time import sleep

browser_catalog = ''
if browser == 'chrome':
    browser_catalog = 'chrome'
elif browser == 'firefox':
    browser_catalog = 'firefox'


def set_site_width(width):
    driver.set_window_size(width, 768)
    real_width = driver.execute_script('return (window.outerWidth - window.innerWidth) + window.outerWidth')

    print('real width = ' + str(driver.execute_script('return (window.outerWidth - window.innerWidth) + window.outerWidth')))
    driver.set_window_size(real_width, 768)



#*************  WIDTH = 1024px  *********************

#main page
get('https://www.restaurantsupply.com/')
set_site_width(1024)
sleep(1)
fullpage_screenshot(browser_catalog +'/w1024/1-main_page2.png')

# #DAP = On Gesture
# get('https://www.restaurantsupply.com/berkel-mb-3-8')
# sleep(1)
# fullpage_screenshot(browser_catalog +'/w1024/2-on_gesture.png')
#
# #DAP = In Cart
# get('https://www.restaurantsupply.com/amana-rfs18ts-medium-duty-stainless-steel-commercial-microwave-with-push-button-controls-208-230v-1800w')
# sleep(1)
# fullpage_screenshot(browser_catalog +'/w1024/3-in_cart.png')
#
# #DAP = Before Order Confirmation
# get('https://www.restaurantsupply.com/manitowoc-jc-0995')
# sleep(1)
# fullpage_screenshot(browser_catalog +'/w1024/4-before_order_confirmation.png')