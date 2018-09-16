import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Calculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.math.com/students/calculators/source/basic.htm')

    def tearDown(self):
        self.driver.quit()

    def enter_random_num(self):
        number = random.randint(0,999)
        numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                   9: 'nine'}
        list_of_numbers = list(str(number))

        for num in list_of_numbers:
            self.driver.find_element(By.NAME, '{}'.format(numbers[float(num)])).click()
        return float(number)


    def test_add_numbers(self):
        operand = random.choice(['+','/','-','x'])
        operands = {'/':'div', '+':'plus', '-':'minus','x':'times'}
        doit = 'DoIt'
        clear = 'clear'

        x = self.enter_random_num()

        self.driver.find_element(By.NAME, '{}'.format(operands[operand])).click()

        y = self.enter_random_num()

        self.driver.find_element(By.NAME, doit).click()

        result = self.driver.find_element(By.NAME, 'Input').get_attribute('value')

        if operand == '+':
            expected_result = x + y
        elif operand == '-':
            expected_result = x - y
        elif operand == '/':
            if y == 0:
                expected_result = 'Infinity'
            else:
                expected_result = x / float(y)
        elif operand == 'x':
            expected_result = x * y

        self.assertEqual(expected_result, float(result))

if __name__ == '__main__':
    unittest.main()
