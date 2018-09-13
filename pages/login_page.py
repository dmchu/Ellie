class LoginPage():
    def __init__(self,driver):
        self.driver = driver


    def login(self, username='admin', password='Password'):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id('btnLogin').click()
