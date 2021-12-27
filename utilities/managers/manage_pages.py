import allure
from page_objects.desktop.calculator_page import CalculatorPage

calc_page = None


class ManagePages:

    @staticmethod
    @allure.step("Initialization pages.")
    def init_desktop_pages():
        globals()['calc_page'] = CalculatorPage()