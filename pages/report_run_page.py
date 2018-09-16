from selenium.webdriver.common.by import By


    def __init__(self,driver):

    def get_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.head h1').text

    def go_to_pim_page(self):
        self.driver.find_element(By.ID, 'menu_pim_viewPimModule').click()

