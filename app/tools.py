from config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from random import randint, choice


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

    @staticmethod
    def invisible(element):
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH, element))
        )

    @staticmethod
    def visible(element):
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, element))
        )


#RANDOM

class Random():
    @staticmethod
    def name():
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        name = 'Test'
        rand_num = randint(5, 15)
        for i in range(0, rand_num):
            name += choice(alpha)
        return name

    @staticmethod
    def email():
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        name = ''
        rand_num = randint(5, 15)
        for i in range(0, rand_num):
            name += choice(alpha)
        return name + '@' + 'test.com'

    @staticmethod
    def phone():
        num = '0123456789'
        phone = ''
        rand_num = randint(12, 15)
        for i in range(0, rand_num):
            phone += choice(num)
        return phone