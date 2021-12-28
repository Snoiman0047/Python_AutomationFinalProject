import allure

from extensions.ui_actions import WebUiAction
from page_objects.appium.appium_page import appium_page
from utilities import base


class mobile_work_flow:
    @staticmethod
    @allure.step("loan calculator")
    def loan_calc(la,ir,ly,lm,epm):
        WebUiAction.click_on(base.app_page.loan_calc)
        WebUiAction.send_keys(base.app_page.loan_amount, la)
        WebUiAction.send_keys(base.app_page.interest_rate, ir)
        WebUiAction.send_keys(base.app_page.loan_year, ly)
        WebUiAction.send_keys(base.app_page.loan_month, lm)
        WebUiAction.send_keys(base.app_page.extra_per_month, epm)
        WebUiAction.click_on(base.app_page.calc)

    @staticmethod
    @allure.step("loan calculator")
    def monthly_payment():
        return WebUiAction.get_text(base.app_page.monthly_payment)

    @staticmethod
    @allure.step("return text of total payment")
    def total_payment():
        return WebUiAction.get_text(base.app_page.total_payment)

    @staticmethod
    @allure.step("return text of total interest")
    def total_interest():
        return WebUiAction.get_text(base.app_page.total_interest)

    @staticmethod
    @allure.step("return text of annual payment")
    def annual_payment():
        return WebUiAction.get_text(base.app_page.annual_payment)

    @staticmethod
    @allure.step("return text of interest saving ")
    def interest_saving():
        return WebUiAction.get_text(base.app_page.interest_saving)






