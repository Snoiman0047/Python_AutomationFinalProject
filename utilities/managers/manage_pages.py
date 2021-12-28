import allure
from page_objects.desktop.calculator_page import CalculatorPage
from page_objects.electron.demos_page import DemosPage
from utilities import base


class ManagePages:

    @staticmethod
    @allure.step('Initialization desktop pages.')
    def init_desktop_pages():
        base.calc_page = CalculatorPage()

    @staticmethod
    @allure.step('Initialization desktop pages.')
    def init_electron_pages():
        base.demos_page = DemosPage()