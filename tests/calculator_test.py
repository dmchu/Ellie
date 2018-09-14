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



    def test_add_numbers(self):
        x = random.randint(0,9)
        y = random.randint(0,9)
        operand = random.choice(['+','/','-','x'])
        numbers = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
        operands = {'/':'div', '+':'plus', '-':'minus','x':'times'}
        doit = 'DoIt'
        clear = 'clear'

        self.driver.find_element(By.NAME, '{}'.format(numbers[x])).click()

        self.driver.find_element(By.NAME, '{}'.format(operands[operand])).click()

        self.driver.find_element(By.NAME, '{}'.format(numbers[y])).click()


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


        # Alternative
        # if operand == 'x':
        #     operand_2 = '*'
        # else:
        #     operand_2 = operand
        #
        # if operand_2 == '/' and y == 0:
        #     expected_result_2 = 'Infinity'
        #
        # expected_result_2 = eval('{} {} float({})'.format(x,operand_2,y))
        #
        # self.assertEqual(expected_result_2, float(result))



if __name__ == '__main__':
    unittest.main()
