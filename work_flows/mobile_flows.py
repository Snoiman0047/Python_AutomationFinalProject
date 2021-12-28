import allure

from extensions.ui_actions import UiAction
from page_objects.appium.appium_page import appium_page
from utilities import base


class mobile_work_flow:
    @staticmethod
    @allure.step("loan calculator")
    def loan_calc(la,ir,ly,lm,epm):
        UiAction.click_on(base.app_page.loan_calc)
        UiAction.send_keys(base.app_page.loan_amount, la)
        UiAction.send_keys(base.app_page.interest_rate, ir)
        UiAction.send_keys(base.app_page.loan_year, ly)
        UiAction.send_keys(base.app_page.loan_month, lm)
        UiAction.send_keys(base.app_page.extra_per_month, epm)
        UiAction.click_on(base.app_page.calc)

    @staticmethod
    @allure.step("return text of monthly payment")
    def monthly_payment():
        return UiAction.get_text(base.app_page.monthly_payment)

    @staticmethod
    @allure.step("return text of total payment")
    def total_payment():
        return UiAction.get_text(base.app_page.total_payment)

    @staticmethod
    @allure.step("return text of total interest")
    def total_interest():
        return UiAction.get_text(base.app_page.total_interest)

    @staticmethod
    @allure.step("return text of annual payment")
    def annual_payment():
        return UiAction.get_text(base.app_page.annual_payment)

    @staticmethod
    @allure.step("return text of interest saving ")
    def interest_saving():
        return UiAction.get_text(base.app_page.interest_saving)






