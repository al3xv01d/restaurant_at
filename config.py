from selenium import webdriver

browser = 'chrome'
server = 'prod'

user = 'altest2@yandex.com'
password = 'Testusa1'

admin_user = ''
admin_password = ''

is_logged = False

#----------------------------

#driver creation
if browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "ie":
    driver = webdriver.Ie()


# BASE URL
if server == 'dev':
    base_url = 'http://dev.restaurantsupply.com/'
elif server == 'stage':
    base_url = 'http://stage.restaurantsupply.com/'
elif server == 'prod':
    base_url = 'https://restaurantsupply.com/'

product = base_url + '/bloomfield-8543-d2'
product_with_related = base_url + '/bloomfield-8543-d2'
category = base_url + '/bloomfield-commercial-coffee-makers-brewers-pourover'