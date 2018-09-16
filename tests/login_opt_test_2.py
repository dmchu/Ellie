import unittest
from selenium import webdriver

from fixtures.base import AdminLoginTestCase
from steps.common import login, welcome_message_method, error_message_method


class MyTestCase(AdminLoginTestCase):

    def setUp(self):
        super(MyTestCase,self).setUp()

    def test_valid_login(self):
        welcome_txt = welcome_message_method(self.driver)
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
