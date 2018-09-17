from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import EXPLICIT_TIMEOUT
from menus.main_menu import MainMenu


class BasePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)

        self.main_menu = MainMenu(self.driver)

        self.page_url = None

    def goto_page(self):
        self.driver.get(self.page_url)

    def get_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.head h1').text