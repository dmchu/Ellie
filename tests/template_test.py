import unittest
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import login, welcome_message_method, logout


class ReportCreate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrm.seleniumminutes.com')
        self.wait = WebDriverWait(self.driver,10)

    def test_create_report(self):
        driver = self.driver
        wait = self.wait
        # Login
        login(driver)



        # logout
        logout(driver)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()