import unittest
from time import sleep

from selenium.webdriver.common.by import By

from fixtures.base import POMAdminLoginTestCase
from menus.main_menu import MainMenu
from pages import base_page
from pages.base_page import BasePage


class MenuTestCase(POMAdminLoginTestCase):
    def test_localization_menu_button(self):

        main_menu = MainMenu(self.driver)
        main_menu.selectLocalization()
        # check the head name
        self.assertEqual("Localization", self.driver.find_element(By.ID, "localizationHeading").text)
        # check the url
        self.assertTrue(self.driver.current_url.find('localization') > 0)

    def test_recruitment_menu(self):
        main_menu = MainMenu(self.driver)
        base_page = BasePage(self.driver)
        main_menu.selectRecruitment()
        header = base_page.get_header()
        self.assertEqual('Candidates',header)

        self.driver.set_window_size(100,100)
        # If the window is small there is no way to click by standard way
        # self.driver.find_element_by_link_text("Vacancies").click()
        # The only way is to use JS query
        # self.driver.execute_script("document.querySelector('#menu_recruitment_viewJobVacancy').click()")
        # OR the easier way
        self.driver.execute_script('arguments[0].click()', self.driver.find_element_by_link_text("Vacancies"))

        header = base_page.get_header()
        self.assertEqual('Vacancies', header)






if __name__ == '__main__':
    unittest.main()
