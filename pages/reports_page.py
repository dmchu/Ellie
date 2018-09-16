from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage

locators = {
    'add_button': (By.ID, "btnAdd"),
    'search_textfield': (By.ID, "search_search"),
    'search_button': (By.CLASS_NAME, "searchBtn"),
    'delete_button': (By.ID, "btnDelete"),
    'dialog_delete_button': (By.ID, "dialogDeleteBtn")
}

class ReportsPage(BasePage):
    def __init__(self,driver):
        super(ReportsPage, self).__init__(driver)
        page_url = '/symfony/web/index.php/core/viewDefinedPredefinedReports/reportGroup/3/reportType/PIM_DEFINED'

    def add_report(self):
        self.driver.find_element(locators['add_button'][0],locators['add_button'][1]).click()

    def search(self, report_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "search_search"))).send_keys(report_name)
        self.driver.find_element(By.CLASS_NAME, "searchBtn").click()

    def run(self, report_name):
        self.driver.find_element(By.XPATH,
                            "//*[@id='resultTable']//td[text() = '{}']/../td[3]/a".format(report_name)).click()

    def report_delete(self):
        self.driver.find_element(By.CSS_SELECTOR, 'td>input').click()
        self.driver.find_element(By.ID, "btnDelete").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "dialogDeleteBtn"))).click()

    def find_report_name(self,report_name):
        return self.driver.find_element(By.XPATH, "//*[@id='resultTable']//td[text() = '{}']/../td[3]/a".format(report_name))