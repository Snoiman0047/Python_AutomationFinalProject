import allure
from page_objects.desktop.calculator_page import CalculatorPage
from page_objects.appium.appium_page import appium_page

calc_page = None

#mobile
app_page = None


class ManagePages:
    @staticmethod
    @allure.step("Initialization pages.")
    def init_desktop_pages():
        globals()['calc_page'] = CalculatorPage()

    @staticmethod
    @allure.step("Initialization pages mobile.")
    def init_mobile_pages():
        globals()['app_page'] = appium_page()