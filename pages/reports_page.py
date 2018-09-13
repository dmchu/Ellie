from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class ReportsPage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_report(self):
        self.driver.find_element(By.ID, "btnAdd").click()

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