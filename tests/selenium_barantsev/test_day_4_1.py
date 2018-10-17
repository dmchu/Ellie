import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LeftMenu(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ['--start-fullscreen']}})
        self.driver.get("http://localhost/litecart/admin")
        self.wait = WebDriverWait(self.driver,10)

    def test_left_menu(self):
        driver = self.driver

        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

        WebDriverWait(driver, 5).until(EC.title_is("My Store"))

        menu = driver.find_element_by_id("box-apps-menu")
        menu_items = []
        for menu_name in menu.find_elements_by_css_selector('.name'):
            menu_items.append(menu_name.text)
        for menu_item in menu_items:
            driver.find_element_by_link_text(menu_item).click()
            self.assertTrue(driver.find_element_by_tag_name('h1').is_displayed())

            sub_menu_items = []
            for sub_menu_name in driver.find_elements_by_css_selector('.docs .name'):
                sub_menu_items.append(sub_menu_name.text)
            for sub_menu_item in sub_menu_items:
                driver.find_element_by_link_text(sub_menu_item).click()
                self.assertTrue(driver.find_element_by_tag_name('h1').is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
