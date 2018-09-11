import unittest
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrm.seleniumminutes.com')
        self.wait = WebDriverWait(self.driver,10)

    def test_something(self):
        empId = randint(1000000,9999999)
        first_name = "Taras"
        last_name = "Bulba"
        job_title = 'QA Engineer'
        employment_status = 'Full-time'

        # Login
        driver = self.driver
        wait = self.wait
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')
        driver.find_element_by_id('btnLogin').click()
        logo = (By.CSS_SELECTOR, "#branding img")
        wait.until(expected_conditions.presence_of_element_located(logo))
        welcome_txt=driver.find_element_by_id('welcome').text
        # Expected value vs actual value
        self.assertEqual('Welcome Admin', welcome_txt)
        driver.find_element_by_link_text('PIM').click()
        add_btn = (By.CSS_SELECTOR, "#btnAdd")
        wait.until(expected_conditions.presence_of_element_located(add_btn))
        # Click the add buttom
        # TODO BY: May need to rerurn and do 'something'
        driver.find_element_by_id('btnAdd').click()

        # Enter first and last name
        driver.find_element_by_id('firstName').send_keys(first_name)
        driver.find_element_by_id('lastName').send_keys(last_name)

        # Enter and remember empId
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys(empId)

        # Save the employee
        driver.find_element_by_id('btnSave').click()

        # Add Job
        left_menu_item = driver.find_element_by_id('sidenav')
        left_menu_item.find_element_by_link_text('Job').click()
        driver.find_element_by_id('btnSave').click()

        Select(driver.find_element_by_id('job_job_title')).select_by_visible_text(job_title)
        Select(driver.find_element_by_id('job_emp_status')).select_by_visible_text(employment_status)
        driver.find_element_by_id('btnSave').click()

        locator = (By.CSS_SELECTOR,".message.success")
        wait.until(expected_conditions.presence_of_element_located(locator))

        # Go to PIM page
        # TODO BY: May need to rerurn and do 'something' as well :P
        driver.find_element_by_id('menu_pim_viewPimModule').click()

        serch_form = (By.CSS_SELECTOR, "#employee-information  h1")
        wait.until(expected_conditions.presence_of_element_located(serch_form))

        # Search by empId
        driver.find_element_by_id('empsearch_id').send_keys(empId)
        driver.find_element_by_id('searchBtn').click()

        # Expected correct full name
        first_name_act = driver.find_element_by_xpath('//td[3]/a').text
        last_name_act = driver.find_element_by_xpath('//td[4]/a').text
        job_title_act = driver.find_element_by_xpath('//td[5]').text
        employment_status_act = driver.find_element_by_xpath('//td[6]').text

        self.assertEqual(first_name,first_name_act)
        self.assertEqual(last_name,last_name_act)
        self.assertEqual(job_title,job_title_act)
        self.assertEqual(employment_status,employment_status_act)

        # Expected: 1 record back
        lst = driver.find_elements_by_xpath('//td[4]/a')
        self.assertTrue(len(lst)==1)

        # delete employee


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()