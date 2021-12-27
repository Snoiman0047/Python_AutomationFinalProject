import allure
from page_objects.desktop.calculator_page import CalculatorPage
from utilities import base


class ManagePages:

    @staticmethod
    @allure.step("Initialization pages.")
    def init_desktop_pages():
        base.calc_page = CalculatorPage()
