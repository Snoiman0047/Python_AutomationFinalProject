import allure

from utilities import base


class UI_Actions:

    @staticmethod
    @allure.step('Click action.')
    def click(elem):
        elem.click()

    @staticmethod
    @allure.step('Get element text.')
    def get_element_text(elem):
        return elem.text

    @staticmethod
    @allure.step("Send keys to Input")
    def send_keys(elem, input):
        elem.send_keys(input)

    @staticmethod
    @allure.step("eyes check window")
    def eyes_check_window(string):
        base.eyes.check_window(string)

    @staticmethod
    @allure.step("Get input value")
    def get_attribute_value(elem):
        return elem.get_attribute("value")

    @staticmethod
    @allure.step("Get Element Text in List By index")
    def get_list_element_text_by_index(list, index):
        return list[index].text[:-7]

    @staticmethod
    @allure.step("Check if element displayed")
    def get_if_element_displayed(elem):
        return elem.is_displayed()
