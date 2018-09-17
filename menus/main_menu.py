from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import EXPLICIT_TIMEOUT


class MainMenu(object):
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)
        self.actions = ActionChains(self.driver)

    def selectLocalization(self):
        driver = self.driver

        self.actions.move_to_element(driver.find_element_by_id("menu_admin_viewAdminModule"))
        self.actions.move_to_element(driver.find_element_by_id("menu_admin_UserManagement"))
        self.actions.move_to_element(driver.find_element_by_id("menu_admin_Configuration"))
        self.actions.click(driver.find_element_by_id("menu_admin_localization")).perform()

    def selectRecruitment(self):
        driver = self.driver
        driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").click()




