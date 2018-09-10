import unittest
from random import randint
from time import sleep

from selenium import webdriver


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrm.seleniumminutes.com')


    def test_something(self):
        empId = randint(1000000,9999999)

        # Login
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')
        driver.find_element_by_id('btnLogin').click()
        sleep(2)
        driver.find_element_by_link_text('PIM').click()
        sleep(2)
        # Click the add buttom
        # TODO BY: May need to rerurn and do 'something'
        driver.find_element_by_id('btnAdd').click()

        # Enter first and last name
        driver.find_element_by_id('firstName').send_keys('Taras')
        driver.find_element_by_id('lastName').send_keys('Bulba')

        # Enter and remember empId
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys(empId)

        # Save the employee
        driver.find_element_by_id('btnSave').click()

        # Go to PIM page
        # TODO BY: May need to rerurn and do 'something' as well :P
        driver.find_element_by_id('menu_pim_viewPimModule').click()
        sleep(2)

        # Search by empId
        driver.find_element_by_id('empsearch_id').send_keys(empId)
        driver.find_element_by_id('searchBtn').click()

        # Expected correct full name
        first_name = driver.find_element_by_xpath('//td[3]/a').text
        last_name = driver.find_element_by_xpath('//td[4]/a').text
        self.assertEqual("Taras",first_name)
        self.assertEqual("Bulba",last_name)

        # Expected: 1 record back
        lst = driver.find_elements_by_xpath('//td[4]/a')
        self.assertTrue(len(lst)==1)
        sleep(2)

        # delete employee


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
