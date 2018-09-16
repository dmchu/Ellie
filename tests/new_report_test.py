import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.new_report_page import NewReportPage


class ReportCreate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)

        self.login_page = LoginPage(self.driver)
        self.new_report_page = NewReportPage(self.driver)
        self.logout_page = LogoutPage(self.driver)

        # self.driver.get('http://hrm.seleniumminutes.com')
        self.login_page.goto_page()

    def test_create_report(self):
        self.login_page.login()
        self.new_report_page.goto_page()
        current_page_url = self.driver.current_url


    def tearDown(self):
        self.logout_page.logout()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
