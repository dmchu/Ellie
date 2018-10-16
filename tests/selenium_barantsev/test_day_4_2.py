import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LeftMenu(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ['--start-fullscreen']}})
        self.driver.get("http://localhost/litecart")
        self.wait = WebDriverWait(self.driver,10)

    def test_stikers(self):
        driver = self.driver
        goods = driver.find_elements_by_class_name('name')
        for good in goods:
            sticker_numbers = len(good.find_elements_by_xpath(".//../div/div"))
            self.assertTrue(sticker_numbers == 1, "Number of stickers is not one!")
            self.assertTrue(good.find_element_by_xpath(".//../div/div").is_displayed(), "Sticker is not displayed!")
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()