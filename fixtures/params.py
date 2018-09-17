import os

cwd = os.path.abspath(os.getcwd())

DOMAIN = 'http://hrm.seleniumminutes.com'
DEFAULT_PASSWORD = 'Password'
BROWSER_TYPE = 'Chrome'
CHROME_EXPATH = os.path.join(cwd, '../browser_drivers/chromedriver')
FIREFOX_EXPATH = os.path.join(cwd, 'browser_drivers/geckodriver')
EXPLICIT_TIMEOUT = 2
# SLOW_TIMEOUT = 10  example of other timeouts
