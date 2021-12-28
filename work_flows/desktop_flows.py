import allure
from extensions.ui_actions import UI_actions
from extensions.verifications import Verifications
from utilities import base


class CalculatorFlows:

    @staticmethod
    @allure.step("Get calculation result.")
    def get_calc_result():
        return UI_actions.get_element_text(base.calc_page.get_calc_result_field()).replace('Display is', '').strip()

    @staticmethod
    @allure.step("Calculating an arithmetic exercise.")
    def calc_it(exercise):
        for ch in exercise:
            CalculatorFlows.number_detection(int(ch)) if ch.isdigit() else CalculatorFlows.char_detection(ch)
        UI_actions.click(base.calc_page.get_equals_btn())

    @staticmethod
    @allure.step("Identify a number and send for click")
    def number_detection(num):
        if num == 1: UI_actions.click(base.calc_page.get_one_btn())
        elif num == 2: UI_actions.click(base.calc_page.get_two_btn())
        elif num == 3: UI_actions.click(base.calc_page.get_three_btn())
        elif num == 4: UI_actions.click(base.calc_page.get_four_btn())
        elif num == 5: UI_actions.click(base.calc_page.get_five_btn())
        elif num == 6: UI_actions.click(base.calc_page.get_six_btn())
        elif num == 7: UI_actions.click(base.calc_page.get_seven_btn())
        elif num == 8: UI_actions.click(base.calc_page.get_eight_btn())
        elif num == 9: UI_actions.click(base.calc_page.get_nine_btn())
        elif num == 0: UI_actions.click(base.calc_page.get_zero_btn())
        else: raise Exception('An unexpected error occurred.')

    @staticmethod
    @allure.step("Identify a arithmetic action and send for click")
    def char_detection(ch):
        if ch == '+': UI_actions.click(base.calc_page.get_plus_btn())
        elif ch == '-': UI_actions.click(base.calc_page.get_minus_btn())
        elif ch == '/': UI_actions.click(base.calc_page.get_divide_btn())
        elif ch == '*': UI_actions.click(base.calc_page.get_multiply_btn())
        elif ch == '=': UI_actions.click(base.calc_page.get_equals_btn())
        else: raise Exception('An unexpected error occurred.')

    @staticmethod
    @allure.step("Verify calc result")
    def verify_calc_result(excepted_result, action):
        Verifications.string_value(CalculatorFlows.get_calc_result(), excepted_result,
                                   f'The {action} operation did not work as expected.')

    @staticmethod
    @allure.step('Clear calculator')
    def clear_calculator():
        UI_actions.click(base.calc_page.get_clear_btn())