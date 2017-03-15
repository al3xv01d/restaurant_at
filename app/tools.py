from config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint, choice
from PIL import Image
import time
import os


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

    @staticmethod
    def staleness_of(element):
        WebDriverWait(driver, 60).until(
            EC.staleness_of((By.XPATH, element))
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

#******************* FULL PAGE SCREENSHOT ***********************************


def fullpage_screenshot(file):

        print("Starting chrome full page screenshot workaround ...")

        total_width = driver.execute_script("return window.innerWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return window.outerWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height,viewport_width,viewport_height))
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width,top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "part_{0}.png".format(part)
            print("Capturing {0} ...".format(file_name))

            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            print("Adding to stitched image with offset ({0}, {1})".format(offset[0],offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        stitched_image.save(file)
        print("Finishing chrome full page screenshot workaround...")
        return True


def set_site_width(width):
    driver.set_window_size(width, 900)
    real_width = driver.execute_script('return (window.outerWidth - window.innerWidth) + window.outerWidth')
    driver.set_window_size(real_width, 900)

