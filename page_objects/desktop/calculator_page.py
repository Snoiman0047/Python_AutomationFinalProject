from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_four(self):
        return self.driver.find_element(By.NAME, 'Four')

    FIELD_CALC_RESULT = (By.XPATH, "//*[@AutomationId='CalculatorResults']")
    BTN_EQUALS = (By.NAME, 'Equals')
    BTN_MINUS = (By.NAME, 'Minus')
    BTN_PLUS = (By.NAME, 'Plus')
    BTN_DIVIDE = (By.NAME, 'Divide by')
    BTN_MULTIPLY = (By.NAME, 'Multiply by')
    BTN_CLEAR = (By.XPATH, "//*[@AutomationId='clearButton']")

    BTN_ZERO = (By.NAME, 'Zero')
    BTN_ONE = (By.NAME, 'One')
    BTN_TWO = (By.NAME, 'Two')
    BTN_THREE = (By.NAME, 'Three')
    BTN_FOUR = (By.NAME, 'Four')
    BTN_FIVE = (By.NAME, 'Five')
    BTN_SIX = (By.NAME, 'Six')
    BTN_SEVEN = (By.NAME, 'Seven')
    BTN_EIGHT = (By.NAME, 'Eight')
    BTN_NINE = (By.NAME, 'Nine')




