import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.base import POMAdminLoginTestCase


class TableSort(POMAdminLoginTestCase):

    def test_table_sort(self):
        driver = self.driver

        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_xpath("//th[3]/a").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//th[3]/a[@class='ASC']")))

        previous_name = ''

        while True:
            all_name_elements = driver.find_elements_by_xpath("//td[3]/a")

            for name_element in all_name_elements:
                current_name = name_element.text

                self.assertGreaterEqual(current_name, previous_name)

                previous_name  = current_name

            if len(driver.find_elements_by_css_selector(".paging.top .desc")) == 0:
                break
            paging = driver.find_element_by_css_selector(".paging.top .desc").text
            paging_parts = paging.split(' of ')

            if paging_parts[-1] in paging_parts[0]:
                break

            driver.find_element_by_css_selector(".paging.top .next a").click()



if __name__ == '__main__':
    unittest.main()