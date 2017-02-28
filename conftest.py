import pytest
from app.app import App
from config import is_logged, base_url, driver


browser = None

@pytest.fixture(scope="session", autouse=True)
def app(request):

    global browser

    if browser is None:
        browser = App()

    # if is_logged == True:
    #     get(base_url)
    #     index = Index()
    #     index.login()

    def fin():
        global browser
        browser.destroy()
        browser = None

    request.addfinalizer(fin)
    return browser

@pytest.fixture(scope="function", autouse=True)
def delete_cookies(request):

    def fin():
        if browser is not None:
            browser.wd.delete_all_cookies()
    request.addfinalizer(fin)