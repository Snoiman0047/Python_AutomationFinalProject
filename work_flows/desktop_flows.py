import allure
from extensions.ui_actions import UI_actions
from extensions.verifications import Verifications
from utilities import base


class CalculatorFlows:
    @staticmethod
    @allure.step("Get calculation result.")
    def get_calc_result():
        return UI_actions.get_element_text(base.calc_page.FIELD_CALC_RESULT).replace('Display is', '').strip()

    @staticmethod
    @allure.step("Calculating an arithmetic exercise.")
    def calc_it(exercise):
        for ch in exercise:
            CalculatorFlows.number_detection(int(ch)) if ch.isdigit() else CalculatorFlows.char_detection(ch)
        UI_actions.click(base.calc_page.BTN_EQUALS)

    @staticmethod
    @allure.step("Identify a number and send for click")
    def number_detection(num):
        if num == 1:
            UI_actions.click(base.calc_page.BTN_ONE)
        elif num == 2:
            UI_actions.click(base.calc_page.BTN_TWO)
        elif num == 3:
            UI_actions.click(base.calc_page.BTN_THREE)
        elif num == 4:
            UI_actions.click(base.calc_page.get_btn_four())
        elif num == 5:
            UI_actions.click(base.calc_page.BTN_FIVE)
        elif num == 6:
            UI_actions.click(base.calc_page.BTN_SIX)
        elif num == 7:
            UI_actions.click(base.calc_page.BTN_SEVEN)
        elif num == 8:
            UI_actions.click(base.calc_page.BTN_EIGHT)
        elif num == 9:
            UI_actions.click(base.calc_page.BTN_NINE)
        elif num == 0:
            UI_actions.click(base.calc_page.BTN_ZERO)
        else:
            raise Exception('An unexpected error occurred.')

    @staticmethod
    @allure.step("Identify a arithmetic action and send for click")
    def char_detection(ch):
        if ch == '+':
            UI_actions.click(base.calc_page.BTN_PLUS)
        elif ch == '-':
            UI_actions.click(base.calc_page.BTN_MINUS)
        elif ch == '/':
            UI_actions.click(base.calc_page.BTN_DIVIDE)
        elif ch == '*':
            UI_actions.click(base.calc_page.BTN_MULTIPLY)
        elif ch == '=':
            UI_actions.click(base.calc_page.BTN_EQUALS)
        else:
            raise Exception('An unexpected error occurred.')

    @staticmethod
    @allure.step("Verify calc result")
    def verify_calc_result(excepted_result, action):
        Verifications.string_value(CalculatorFlows.get_calc_result() == excepted_result,
                                   f'The {action} operation did not work as expected.')

    @staticmethod
    @allure.step('Clear calculator')
    def clear_calculator():
        UI_actions.click(base.calc_page.BTN_CLEAR)
