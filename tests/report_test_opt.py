import unittest
from random import randint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.new_report_page import NewReportPage
from pages.pim_page import PimPage
from pages.report_run_page import ReportRunPage
from pages.reports_page import ReportsPage


class ReportCreate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://hrm.seleniumminutes.com')

        self.wait = WebDriverWait(self.driver, 10)
        self.login_page = LoginPage(self.driver)
        self.pim_page = PimPage(self.driver)
        self.reports_page = ReportsPage(self.driver)
        self.new_report_page = NewReportPage(self.driver)
        self.report_run_page = ReportRunPage(self.driver)
        self.logout_page = LogoutPage(self.driver)

    def test_create_report(self):
        report_name = "DC report: " + str(randint(1, 100))
        selection_ctiteria = 'Job Title'
        display_field_group = 'Personal '
        expected_report_header = 'Report Name : {}'.format(report_name)

        self.login_page.login()
        self.pim_page.go_to_reports_page()
        self.reports_page.add_report()
        self.new_report_page.set_report_name(report_name)
        self.new_report_page.select_selection_criteria(selection_ctiteria)
        self.new_report_page.select_display_field_group(display_field_group)
        self.new_report_page.enable_display_fields()
        self.new_report_page.save()
        self.assertTrue(self.reports_page.find_report_name(report_name))
        self.report_name = report_name
        self.reports_page.search(report_name)
        self.reports_page.run(report_name)
        report_header = self.report_run_page.get_header()
        self.assertEqual(expected_report_header,report_header)

    def tearDown(self):
        if self.report_name:
            self.report_run_page.go_to_pim_page()
            self.pim_page.go_to_reports_page()
            self.reports_page.search(self.report_name)
            self.reports_page.report_delete()
            self.logout_page.logout()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()