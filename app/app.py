from config import driver


class App:

    wd = driver

    def __init__(self):
        self.wd.maximize_window()
      #  self.wd.implicitly_wait(60)
       # self.wd.set_page_load_timeout(60)

    def destroy(self):
        self.wd.quit()

    def hover(self):
        pass
