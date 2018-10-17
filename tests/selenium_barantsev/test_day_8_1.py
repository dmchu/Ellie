import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ['--start-fullscreen']}})
        self.driver.get("http://localhost/litecart/admin")
        self.wait = WebDriverWait(self.driver,10)

    def test_external_links(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)


        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()
        wait.until(EC.title_is("My Store"))

        menu = driver.find_element_by_id("box-apps-menu")
        menu.find_element(By.LINK_TEXT, "Countries").click()
        wait.until(EC.title_contains("Countries"))

        table = driver.find_element(By.CSS_SELECTOR, "table.dataTable")
        rows = table.find_elements(By.CSS_SELECTOR, ".row")

        countries = [row.find_element(By.TAG_NAME, 'a').text for row in rows]

        country = random.randrange(0, (len(countries)))

        driver.find_element(By.LINK_TEXT, countries[country]).click()

        external_links = driver.find_elements(By.CLASS_NAME, "fa-external-link")

        old_window = driver.current_window_handle
        new_window = None

        for external_link in external_links:
            external_link.click()
            wait.until(EC.new_window_is_opened)
            current_windows = driver.window_handles
            for window_id in current_windows:
                if window_id != old_window:
                    new_window = window_id

            driver.switch_to.window(new_window)
            driver.close()
            driver.switch_to.window(old_window)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()