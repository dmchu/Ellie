from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LogoutPage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def logout(self):
        self.driver.find_element_by_id('welcome').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()
