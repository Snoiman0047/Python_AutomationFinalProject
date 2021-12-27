import allure
from utilities import base


class UI_actions:

    @staticmethod
    @allure.step('Click action.')
    def click(elem):
        UI_actions.find_element(elem).click()

    @staticmethod
    @allure.step('Find element.')
    def find_element(elem):
        return base.driver.find_element(elem[0], elem[1])

    @staticmethod
    @allure.step('Get element text.')
    def get_element_text(elem):
        return UI_actions.find_element(elem).text
