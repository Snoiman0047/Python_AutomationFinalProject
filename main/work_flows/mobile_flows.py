import allure

from main.extensions.ui_actions import UIActions
from main.utilities import base


class mobile_work_flow:
    @staticmethod
    @allure.step("loan calculator")
    def loan_calc(la,ir,ly,lm,epm):
        UIActions.click(base.app_page.loan_calc)
        UIActions.write_input_text(base.app_page.loan_amount, la)
        UIActions.write_input_text(base.app_page.interest_rate, ir)
        UIActions.write_input_text(base.app_page.loan_year, ly)
        UIActions.write_input_text(base.app_page.loan_month, lm)
        UIActions.write_input_text(base.app_page.extra_per_month, epm)
        UIActions.click(base.app_page.calc)

    @staticmethod
    @allure.step("return text of monthly payment")
    def monthly_payment():
        return UIActions.get_element_text(base.app_page.monthly_payment)

    @staticmethod
    @allure.step("return text of total payment")
    def total_payment():
        return UIActions.get_element_text(base.app_page.total_payment)

    @staticmethod
    @allure.step("return text of total interest")
    def total_interest():
        return UIActions.get_element_text(base.app_page.total_interest)

    @staticmethod
    @allure.step("return text of annual payment")
    def annual_payment():
        return UIActions.get_element_text(base.app_page.annual_payment)

    @staticmethod
    @allure.step("return text of interest saving ")
    def interest_saving():
        return UIActions.get_element_text(base.app_page.interest_saving)






