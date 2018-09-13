from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PimPage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_reports_page(self):
        wait = self.wait
        driver = self.driver
        # go to the report tub
        driver.find_element(By.ID, 'menu_pim_viewPimModule').click()
        wait.until(expected_conditions.presence_of_element_located((By.ID, 'menu_core_viewDefinedPredefinedReports'))).click()



