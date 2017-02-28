from config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


def get(url):
    driver.get(url)

def find(locator='', by = 'xpath'):
    element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, locator))
    )
    return element

def hover(element_to_hover):
    pass

#WAIT CLASS ----------------

class Wait():

    @staticmethod
    def is_clickable(self, element):
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, element))
        )
        return element