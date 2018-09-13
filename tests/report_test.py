import unittest
from random import randint

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
        # variables:
        report_name = "DC report: "+ str(randint(1,100))

        # Login
        login(driver)

        # go to the report tub
        driver.find_element(By.ID, 'menu_pim_viewPimModule').click()
        wait.until(expected_conditions.presence_of_element_located((By.ID, 'menu_core_viewDefinedPredefinedReports'))).click()


        # Click on the add button
        driver.find_element(By.ID, "btnAdd").click()

        # Enter unique report name
        wait.until(expected_conditions.presence_of_element_located((By.ID, 'report_report_name'))).send_keys(report_name)

        # Select criteria = job title
        Select(driver.find_element(By.ID, 'report_criteria_list')).select_by_visible_text('Job Title') #select_by_value('job_title')
        driver.find_element(By.ID,'btnAddConstraint').click()
        # select display field group = personal
        Select(driver.find_element(By.ID, 'report_display_groups')).select_by_visible_text('Personal ')
        driver.find_element(By.ID, 'btnAddDisplayGroup').click()

        # make sure to check the ckeckbox and save

        driver.find_element(By.ID,"display_group_1").click()
        driver.find_element(By.ID, 'btnSave').click()

        # verify the report was created
        #self.assertTrue(self.is_element_present(By.XPATH, "//*[@id='resultTable']//td[text() = '{}']/../td[3]/a".format(report_name)))
        self.assertTrue(driver.find_element(By.XPATH, "//*[@id='resultTable']//td[text() = '{}']/../td[3]/a".format(report_name)))

        self.report_name = report_name

        # Run the report
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "search_search"))).send_keys(report_name)
        driver.find_element(By.CLASS_NAME, "searchBtn").click()
        driver.find_element(By.XPATH, "//*[@id='resultTable']//td[text() = '{}']/../td[3]/a".format(report_name)).click()

        # verify the report works
        report_header = driver.find_element(By.CSS_SELECTOR, '.head h1').text
        self.assertEqual('Report Name : {}'.format(report_name),report_header)
        # Tear down: remove the report
        # logout

 #      def is_element_present(self,by,locator):
 #        try:
 #            self.driver.find_element(by,locator)
 #            return True
 #        except NoSuchElementException:
 #            return  False

    def tearDown(self):
        if self.report_name:
            driver = self.driver
            driver.find_element(By.ID, 'menu_pim_viewPimModule').click()
            self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'menu_core_viewDefinedPredefinedReports'))).click()
            self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "search_search"))).send_keys(self.report_name)
            driver.find_element(By.CLASS_NAME, "searchBtn").click()
            driver.find_element(By.CSS_SELECTOR,'td>input').click()
            driver.find_element(By.ID, "btnDelete").click()
            self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "dialogDeleteBtn"))).click()
            logout(driver)
            driver.quit()

if __name__ == '__main__':
    unittest.main()