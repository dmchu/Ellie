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

    def enter_single_num(self):
        numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                   9: 'nine'}
        num = 0

        for digit in range(random.randint(1,3)):
            number = random.randint(0,9)
            self.driver.find_element(By.NAME, '{}'.format(numbers[int(number)])).click()
            num = num*10 + number

        return float(num)


    def test_add_numbers(self):

        operand = random.choice(['+','/','-','x'])
        operands = {'/':'div', '+':'plus', '-':'minus','x':'times'}
        doit = 'DoIt'
        clear = 'clear'

        x = self.enter_single_num()

        self.driver.find_element(By.NAME, '{}'.format(operands[operand])).click()

        y = self.enter_single_num()

        self.driver.find_element(By.NAME, doit).click()

        result = self.driver.find_element(By.NAME, 'Input').get_attribute('value')

        if operand == 'x':
            operand_2 = '*'
        else:
            operand_2 = operand

        if operand_2 == '/' and y == 0:
            expected_result_2 = 'Infinity'

        expected_result_2 = eval('{} {} {}'.format(x,operand_2,y))

        self.assertEqual(expected_result_2, float(result))



if __name__ == '__main__':
    unittest.main()
