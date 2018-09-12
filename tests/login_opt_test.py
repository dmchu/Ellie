import unittest
from selenium import webdriver
from steps.common import login, welcome_message_method, error_message_method


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrm.seleniumminutes.com')

    def test_valid_login(self):
        driver = self.driver
        login(driver)
        welcome_txt = welcome_message_method(driver)
        # Expected value vs actual value
        self.assertEqual('Welcome Admin', welcome_txt)

    def test_invalid_password(self):
        driver = self.driver
        valid_username = 'admin'
        invalid_password = 'password'
        login(driver,valid_username, invalid_password)

        error_msg = error_message_method(driver)
        self.assertEqual('Invalid credentials',error_msg)

    def test_empty_password(self):
        driver = self.driver
        valid_username = 'admin'
        empty_password = ''
        login(driver,valid_username,empty_password)
        error_msg = error_message_method(driver)
        self.assertEqual('Password cannot be empty',error_msg)

if __name__ == '__main__':
    unittest.main()
