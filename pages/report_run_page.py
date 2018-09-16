from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ReportRunPage(BasePage):
    def __init__(self,driver):
        super(ReportRunPage, self).__init__(driver)
        self.page_url = '/symfony/web/index.php/core/viewDefinedPredefinedReports/reportGroup/3/reportType/PIM_DEFINED'

    def get_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.head h1').text

    def go_to_pim_page(self):
        self.driver.find_element(By.ID, 'menu_pim_viewPimModule').click()

