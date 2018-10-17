import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


from mitmproxy import http



class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)


class CountriesOrder(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ['--start-fullscreen']}}),MyListener())
        self.driver.get("http://localhost/litecart/admin")
        self.wait = WebDriverWait(self.driver,10)


    def test_browser_logs(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()
        wait.until(EC.title_is("My Store"))

        menu = driver.find_element_by_id("box-apps-menu")
        menu.find_element(By.LINK_TEXT, "Catalog").click()
        wait.until(EC.title_contains("Catalog"))

        table = driver.find_element(By.CSS_SELECTOR, "table.dataTable")
        table.find_element(By.LINK_TEXT, "Rubber Ducks").click()

        table = driver.find_element(By.CSS_SELECTOR, "table.dataTable")

        rows = table.find_elements(By.CSS_SELECTOR, ".row img ")

        goods = [row.find_element(By.XPATH, "../a").text for row in rows]

        for good in goods:
            driver.find_element(By.LINK_TEXT, good).click()
            menu = driver.find_element_by_id("box-apps-menu")
            menu.find_element(By.LINK_TEXT, "Catalog").click()
            wait.until(EC.title_contains("Catalog"))
            table = driver.find_element(By.CSS_SELECTOR, "table.dataTable")
            table.find_element(By.LINK_TEXT, "Rubber Ducks").click()

        entry = driver.get_log('browser')
        for j, i in enumerate(entry):
            print(j + 1, "<", i["level"], ">", i["message"])

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()