from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'browser': 'Safari', 'browser_version': '10.0', 'os': 'OS X', 'os_version': 'Sierra', 'resolution': '1920x1080'}

driver = webdriver.Remote(
    command_executor='http://vadymantsyferov1:smT8fwsFdxEBsi7bUWcd@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)




test_var = ''