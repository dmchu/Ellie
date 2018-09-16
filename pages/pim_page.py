from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage


class PimPage(BasePage):
    def __init__(self,driver):
        super(PimPage,self).__init__(driver)
        self.page_url = '/symfony/web/index.php/pim/viewEmployeeList'

    def go_to_reports_page(self):
        self.driver.find_element(By.ID, 'menu_pim_viewPimModule').click()
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'menu_core_viewDefinedPredefinedReports'))).click()



