from selenium import webdriver

browser = 'chrome'
server = 'dev'

user = 'altest2@yandex.com'
password = 'Testusa1'

admin_user = '111'
admin_password = '111'

is_logged = False

#----------------------------

#driver creation
if browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "ie":
    driver = webdriver.Ie()
# elif browser == 'safari':
#     desired_cap = {'browser': 'Safari', 'browser_version': '10.0', 'os': 'OS X', 'os_version': 'Sierra',
#                    'resolution': '1920x1080'}
#     driver = webdriver.Remote(
#         command_executor='http://vadymantsyferov1:smT8fwsFdxEBsi7bUWcd@hub.browserstack.com:80/wd/hub',
#         desired_capabilities=desired_cap)


# BASE URL
if server == 'dev':
    base_url = 'http://gomage777:gomage777@dev.restaurantsupply.com'
elif server == 'stage':
    base_url = 'http://gomage777:gomage777@stage.restaurantsupply.com'
elif server == 'prod':
    base_url = 'https://restaurantsupply.com'


if server == 'prod':
    product = base_url + '/bloomfield-8543-d2'
    product_with_related = base_url + '/bloomfield-8543-d2'
    category = base_url + '/bloomfield-commercial-coffee-makers-brewers-pourover'
elif server == 'stage' or server == 'dev':
    product = base_url + '/bloomfield-8543-d2.html'
    product_with_related = base_url + '/bloomfield-8543-d2.html'
    category = base_url + '/electronic-portion-control-scales.html'