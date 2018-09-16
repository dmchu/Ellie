from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.page_url = None

    def goto_page(self):
        self.driver.get(self.page_url)