import pytest
from app.app import App
from config import is_logged, base_url
from app.tools import get, Wait
from time import sleep


browser = None

@pytest.fixture(scope="session", autouse=True)
def app(request):

    global browser

    if browser is None:
        browser = App()

    if is_logged == True:
        get(base_url)
        browser.index_page.login()

    def fin():
        global browser
        browser.destroy()
        browser = None

    request.addfinalizer(fin)
    return browser

#********* USE it if is_logged = FALSE **************
@pytest.fixture(scope="function", autouse=True)
def delete_cookies(request):

    def fin():
        if browser is not None:
            browser.wd.delete_all_cookies()
        else:
            pass

    if not is_logged and browser is not None:
        request.addfinalizer(fin)
    else:
        pass


#********* USE it if is_logged = TRUE **************
@pytest.fixture(scope="function", autouse=True)
def empty_cart(request):

    def fin():
        if browser is not None:

            if 'checkout/cart' not in browser.wd.current_url:
                get(base_url + '/checkout/cart/')
                try:
                    Wait.invisible(browser.cart_page.full_page_loader_lo)
                    browser.cart_page.empty_cart_link.click()
                    sleep(1)
                except Exception as e:
                    Wait.invisible(browser.cart_page.full_page_loader_lo)
                    browser.cart_page.empty_cart_link.click()
                    sleep(1)
            else:
                try:
                    Wait.invisible(browser.cart_page.full_page_loader_lo)
                    browser.cart_page.empty_cart_link.click()
                    sleep(1)
                except Exception as e:
                    Wait.invisible(browser.cart_page.full_page_loader_lo)
                    browser.cart_page.empty_cart_link.click()
                    sleep(1)
        else:
            pass

    if is_logged and browser is not None:
        request.addfinalizer(fin)
    else:
        pass