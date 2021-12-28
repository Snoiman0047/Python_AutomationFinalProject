import allure
from page_objects.desktop.calculator_page import CalculatorPage
from page_objects.appium.appium_page import appium_page
from utilities import base




class ManagePages:
    @staticmethod
    @allure.step("Initialization pages.")
    def init_desktop_pages():
        base.calc_page = CalculatorPage()

    @staticmethod
    @allure.step("Initialization pages mobile.")
    def init_mobile_pages():
        base.app_page = appium_page()