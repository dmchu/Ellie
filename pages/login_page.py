from fixtures.params import DOMAIN, DEFAULT_PASSWORD


class LoginPage():
    def __init__(self,driver):
        self.driver = driver


    def login(self, username='admin', password=DEFAULT_PASSWORD):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id('btnLogin').click()

    def goto_login_page(self):
        # go to the admin page
        self.driver.get(DOMAIN)
        # self.driver.get('http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login')

