import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Goods(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ['--start-fullscreen']}})
        self.driver.get("http://localhost/litecart")
        self.wait = WebDriverWait(self.driver,10)

    def test_goods_items(self):
        driver = self.driver
        wait = self.wait
        driver.get("http://localhost/litecart")

        # Более точно, нужно открыть главную страницу, выбрать первый товар в категории Campaigns и проверить следующее:

        main_page_offers = driver.find_elements(By.CSS_SELECTOR, ".content a.link")
        self.assertTrue(len(main_page_offers) > 0, "There is No offers")

        mp_goods = []

        for current_offer in main_page_offers:
            current_goods_attributs = dict.fromkeys(
                ['text_of_good', 'link_of_good', 'price', 'regular_price', 'campaign_price', 'campaign_price_color',
                 'regular_price_color', 'regular_price_style', 'campaign_price_style'])

            current_goods_attributs['text_of_good'] = current_offer.find_element(By.CLASS_NAME, "name").get_attribute(
                'textContent')
            current_goods_attributs['link_of_good'] = current_offer.get_attribute('href')

            if len(current_offer.find_elements(By.CLASS_NAME, "price")) > 0:
                current_goods_attributs['price'] = current_offer.find_element(By.CLASS_NAME, "price").get_attribute(
                    'textContent')
            else:
                current_goods_attributs['regular_price_style'] = current_offer.find_element(By.CLASS_NAME,
                                                                                            "regular-price").tag_name
                current_goods_attributs['regular_price'] = current_offer.find_element(By.CLASS_NAME,
                                                                                      "regular-price").get_attribute(
                    'textContent')
                current_goods_attributs['regular_price_color'] = current_offer.find_element(By.CLASS_NAME,
                                                                                            "regular-price").value_of_css_property(
                    "color")
                current_goods_attributs['campaign_price_style'] = current_offer.find_element(By.CLASS_NAME,
                                                                                             "campaign-price").tag_name
                current_goods_attributs['campaign_price'] = current_offer.find_element(By.CLASS_NAME,
                                                                                       "campaign-price").get_attribute(
                    'textContent')
                current_goods_attributs['campaign_price_color'] = current_offer.find_element(By.CLASS_NAME,
                                                                                             "campaign-price").value_of_css_property(
                    "color")

            mp_goods.append(current_goods_attributs)

        current_page_goods = []
        for current_page in mp_goods:
            driver.find_element(By.CSS_SELECTOR, 'a.link[href="{}"]'.format(current_page['link_of_good'])).click()

            current_page_attributs = dict.fromkeys(
                ['text_of_good', 'price', 'regular_price', 'campaign_price', 'campaign_price_color',
                 'regular_price_color', 'regular_price_style', 'campaign_price_style'])
            current_page_attributs['text_of_good'] = driver.find_element(By.TAG_NAME, 'h1').text

            # а) на главной странице и на странице товара совпадает текст названия товара
            self.assertTrue(current_page['text_of_good'] == current_page_attributs['text_of_good'],
                       "The goods title text does not mutch")

            if current_page["price"] != None:
                current_page_attributs['price'] = driver.find_element(By.CLASS_NAME, "price").get_attribute(
                    'textContent')

                self.assertTrue(current_page['price'] == current_page_attributs['price'], "The price of good does not mutch")

            else:
                current_page_attributs['regular_price_style'] = driver.find_element(By.CLASS_NAME,
                                                                                    "regular-price").tag_name
                current_page_attributs['regular_price'] = driver.find_element(By.CLASS_NAME,
                                                                              "regular-price").get_attribute(
                    'textContent')
                current_page_attributs['regular_price_color'] = driver.find_element(By.CLASS_NAME,
                                                                                    "regular-price").value_of_css_property(
                    "color")
                current_page_attributs['campaign_price_style'] = driver.find_element(By.CLASS_NAME,
                                                                                     "campaign-price").tag_name
                current_page_attributs['campaign_price'] = driver.find_element(By.CLASS_NAME,
                                                                               "campaign-price").get_attribute(
                    'textContent')
                current_page_attributs['campaign_price_color'] = driver.find_element(By.CLASS_NAME,
                                                                                     "campaign-price").value_of_css_property(
                    "color")

                # б) на главной странице и на странице товара совпадают цены (обычная и акционная)
                self.assertTrue(current_page['regular_price'] == current_page_attributs['regular_price'],
                           "The regular price does not mutch")
                self.assertTrue(current_page['campaign_price'] == current_page_attributs['campaign_price'],
                           "The campaign price does not mutch")

                # в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой,
                #  у которого в RGBa представлении одинаковые значения для каналов R, G и B)

                reg_price_colors = dict(
                    zip(['R', 'G', 'B'], current_page_attributs['regular_price_color'][5:-4].split(", ")))
                self.assertTrue(
                    current_page['regular_price_style'] == 's' and reg_price_colors['R'] == reg_price_colors['G'] ==
                    reg_price_colors['B'],
                    "The regular price is not strike out and not gray")

                # г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
                # (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)

                camp_price_colors = dict(
                    zip(['R', 'G', 'B'], current_page_attributs['campaign_price_color'][5:-4].split(", ")))
                self.assertTrue(
                    camp_price_colors['R'] != 0 and camp_price_colors['G'] == '0' and camp_price_colors['B'] == '0'
                    and current_page_attributs['campaign_price_style'] == 'strong',
                    "The campaign price is not RED and BOLD")

                # д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)

                reg_price_size = driver.find_element(By.CLASS_NAME, "regular-price").size
                cam_price_size = driver.find_element(By.CLASS_NAME, "campaign-price").size
                self.assertTrue((cam_price_size['height'] * cam_price_size['width']) > (
                            reg_price_size['height'] * reg_price_size['width']),
                           "Campaign price is not larger than regular one")

            current_page_goods.append(current_page_attributs)

            driver.find_element(By.CSS_SELECTOR, '*[title="Home"]').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()