from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


def login(driver, username = 'admin', password = 'Password'):
    driver.find_element_by_id('txtUsername').send_keys(username)
    driver.find_element_by_id('txtPassword').send_keys(password)
    driver.find_element_by_id('btnLogin').click()


def welcome_message_method(driver):
    condition = wait(driver, 2).until(EC.presence_of_element_located((By.ID, 'welcome')))
    return condition.text


def error_message_method(driver):
    return driver.find_element_by_id('spanMessage').text