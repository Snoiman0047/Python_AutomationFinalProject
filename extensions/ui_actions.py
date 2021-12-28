import allure
from utilities import base

class WebUiAction:
    @staticmethod
    @allure.step("Click on an element")
    def click_on(elem):
        WebUiAction.find_element(elem).click()


    @staticmethod
    @allure.step("Send keys to Input")
    def send_keys(elem, input):
        WebUiAction.find_element(elem).send_keys(input)

    @staticmethod
    @allure.step('Find element.')
    def find_element(elem):
        return base.driver.find_element(elem[0], elem[1])

    @staticmethod
    @allure.step("Element Text")
    def get_text(elem):
        return WebUiAction.find_element(elem).text

    @staticmethod
    def verify_test(ac, ex):
        assert ac == ex