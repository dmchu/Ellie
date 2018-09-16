import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import DOMAIN, CHROME_EXPATH, EXPLICIT_TIMEOUT, FIREFOX_EXPATH, BROWSER_TYPE
from pages.login_page import LoginPage
from steps.common import login


class BaseTestCase(unittest.TestCase):
    def get_browser(self):
        if BROWSER_TYPE.lower().find('chrome') >= 0:
            webdriver.Chrome(executable_path=CHROME_EXPATH)
        elif BROWSER_TYPE.lower().find('firefox') >= 0:
            webdriver.Firefox(executable_path=FIREFOX_EXPATH)




    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_EXPATH)
        self.wait = WebDriverWait(self.driver,EXPLICIT_TIMEOUT)
        # self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()


class AdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(AdminLoginTestCase, self).setUp()
        self.driver.get(DOMAIN)
        login(self.driver)


    def tearDown(self):
        super(AdminLoginTestCase, self).tearDown()


class POMAdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(POMAdminLoginTestCase, self).setUp()
        self.driver.get(DOMAIN)
        self.login = LoginPage(self.driver)
        self.login.goto_login_page()
        self.login.login()

    def tearDown(self):
        super(POMAdminLoginTestCase, self).tearDown()

if __name__ == '__main__':
    unittest.main()
