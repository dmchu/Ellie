import unittest
from random import randint
from time import sleep

from selenium import webdriver


class LogoSize(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrm.seleniumminutes.com')


    def test_logo_position(self):

        # Login
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')
        driver.find_element_by_id('btnLogin').click()
        sleep(2)
        welcome_txt=driver.find_element_by_id('welcome').text
        # Expected value vs actual value
        self.assertEqual('Welcome Admin', welcome_txt)
        # find logo
        logo = driver.find_element_by_css_selector('#branding img')
        # check logo size
        logo_size = logo.size
        logo_size_expected = {'width':283,'height':56}
        self.assertEqual(56,logo_size['height'])
        self.assertEqual(logo_size_expected,logo_size)
        self.assertTrue(logo_size['width'] == 283 and logo_size['height'] == 56)
        self.assertDictEqual(logo_size_expected,logo_size)
        # check position at top left
        window_size = driver.get_window_size()

        logo_location = logo.location

        top_right_corner_logo_x_location = logo_location['x'] + logo_size['width']
        self.assertTrue(top_right_corner_logo_x_location < window_size['width']/2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()