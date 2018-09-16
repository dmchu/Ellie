<<<<<<< HEAD
from fixtures.params import DOMAIN, DEFAULT_PASSWORD


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
=======
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.page_url = 'http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login'
>>>>>>> page_object_model


    def login(self, username='admin', password=DEFAULT_PASSWORD):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id('btnLogin').click()

    def goto_login_page(self):
        # go to the admin page
        self.driver.get(DOMAIN)
        # self.driver.get('http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login')

