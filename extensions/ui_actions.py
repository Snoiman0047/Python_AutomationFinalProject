import allure
from sanity_tests.conftest import driver


class UI_actions:

    @staticmethod
    @allure.step('Click action.')
    def click(elem):
        UI_actions.find_element(elem).click()

    @staticmethod
    @allure.step('Find element.')
    def find_element(elem):
        driver.find_element(elem)

    @staticmethod
    @allure.step('Get element text.')
    def get_element_text(elem):
        return UI_actions.find_element(elem).text
