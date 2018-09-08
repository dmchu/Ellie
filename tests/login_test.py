import unittest
from time import sleep

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrm.seleniumminutes.com')


    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')
        driver.find_element_by_id('btnLogin').click()
        sleep(2)
        welcome_txt=driver.find_element_by_id('welcome').text

        # Expected value vs actual value
        self.assertEqual('Welcome Admin', welcome_txt)

    def test_invalid_password(self):
        pass


    def test_empty_password(self):
        pass

if __name__ == '__main__':
    unittest.main()
