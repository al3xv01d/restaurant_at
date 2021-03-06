import pytest
from app.app import App
from config import is_logged, base_url, server
from app.tools import get, Wait
from time import sleep


browser = None

@pytest.fixture(scope="session", autouse=True)
def app(request):

    global browser

    if browser is None:
        browser = App()

    # if server == 'stage':
    #     browser.wd.get('http://gomage777:gomage777@stage.restaurantsupply.com')

    if is_logged == True:
        get(base_url)
        browser.index_page.login()
        sleep(3) # значение подгружается через какое-то время, а не при открытии страницы
        if int(browser.index_page.cart_counter_number.text) > 0:
            browser.cart_page.empty_cart()

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
            browser.cart_page.empty_cart()
        else:
            pass

    if is_logged and browser is not None:
        request.addfinalizer(fin)
    else:
        pass