from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

    def __init__(self,driver):

    def set_report_name(self, report_name):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, 'report_report_name'))).send_keys(
            report_name)

    def select_selection_criteria(self, selection_ctiteria):
        Select(self.driver.find_element(By.ID, 'report_criteria_list')).select_by_visible_text(selection_ctiteria)
        self.driver.find_element(By.ID, 'btnAddConstraint').click()

    def select_display_field_group(self, display_field_group):
        Select(self.driver.find_element(By.ID, 'report_display_groups')).select_by_visible_text(display_field_group)
        self.driver.find_element(By.ID, 'btnAddDisplayGroup').click()

    def enable_display_fields(self):
        self.driver.find_element(By.ID, "display_group_1").click()

    def save(self):
        self.driver.find_element(By.ID, 'btnSave').click()

