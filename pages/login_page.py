from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.page_url = 'http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login'


    def login(self, username='admin', password='Password'):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id('btnLogin').click()
