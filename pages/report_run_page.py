from selenium.webdriver.common.by import By


class ReportRunPage():
    def __init__(self,driver):
        self.driver = driver

    def get_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.head h1').text

    def go_to_pim_page(self):
        self.driver.find_element(By.ID, 'menu_pim_viewPimModule').click()