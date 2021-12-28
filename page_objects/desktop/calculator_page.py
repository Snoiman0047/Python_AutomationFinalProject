import allure
from selenium.webdriver.common.by import By


class CalculatorPage:

    __FIELD_CALC_RESULT = (By.XPATH, "//*[@AutomationId='CalculatorResults']")
    __BTN_EQUALS = (By.NAME, 'Equals')
    __BTN_MINUS = (By.NAME, 'Minus')
    __BTN_PLUS = (By.NAME, 'Plus')
    __BTN_DIVIDE = (By.NAME, 'Divide by')
    __BTN_MULTIPLY = (By.NAME, 'Multiply by')
    __BTN_CLEAR = (By.XPATH, "//*[@AutomationId='clearButton']")

    __BTN_ZERO = (By.NAME, 'Zero')
    __BTN_ONE = (By.NAME, 'One')
    __BTN_TWO = (By.NAME, 'Two')
    __BTN_THREE = (By.NAME, 'Three')
    __BTN_FOUR = (By.NAME, 'Four')
    __BTN_FIVE = (By.NAME, 'Five')
    __BTN_SIX = (By.NAME, 'Six')
    __BTN_SEVEN = (By.NAME, 'Seven')
    __BTN_EIGHT = (By.NAME, 'Eight')
    __BTN_NINE = (By.NAME, 'Nine')

    @allure.step('Get calc-result field.')
    def get_calc_result_field(self):
        return self.__FIELD_CALC_RESULT

    @allure.step('Get equals button.')
    def get_equals_btn(self):
        return self.__BTN_EQUALS

    @allure.step('Get minus button.')
    def get_minus_btn(self):
        return self.__BTN_MINUS

    @allure.step('Get plus button.')
    def get_plus_btn(self):
        return self.__BTN_PLUS

    @allure.step('Get divide button.')
    def get_divide_btn(self):
        return self.__BTN_DIVIDE

    @allure.step('Get multiply button.')
    def get_multiply_btn(self):
        return self.__BTN_MULTIPLY

    @allure.step('Get clear button.')
    def get_clear_btn(self):
        return self.__BTN_CLEAR

    @allure.step('Get zero button (0).')
    def get_zero_btn(self):
        return self.__BTN_ZERO

    @allure.step('Get one button (1).')
    def get_one_btn(self):
        return self.__BTN_ONE

    @allure.step('Get two button (2).')
    def get_two_btn(self):
        return self.__BTN_TWO

    @allure.step('Get three button (3).')
    def get_three_btn(self):
        return self.__BTN_THREE

    @allure.step('Get four button (4).')
    def get_four_btn(self):
        return self.__BTN_FOUR

    @allure.step('Get zero button (5).')
    def get_five_btn(self):
        return self.__BTN_FIVE

    @allure.step('Get zero button (6).')
    def get_six_btn(self):
        return self.__BTN_SIX

    @allure.step('Get seven button (7).')
    def get_seven_btn(self):
        return self.__BTN_SEVEN

    @allure.step('Get eight button (8).')
    def get_eight_btn(self):
        return self.__BTN_EIGHT

    @allure.step('Get nine button (9).')
    def get_nine_btn(self):
        return self.__BTN_NINE





