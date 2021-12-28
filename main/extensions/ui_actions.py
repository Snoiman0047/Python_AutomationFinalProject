import allure
from main.utilities import base


class UIActions:

    @staticmethod
    @allure.step('Click action.')
    def click(elem):
        if type(elem) == tuple:
            UIActions.find_element(elem).click()
        else: elem.click()

    @staticmethod
    @allure.step('Find element.')
    def find_element(elem):
        return base.driver.find_element(elem[0], elem[1])

    @staticmethod
    @allure.step('Get element text.')
    def get_element_text(elem):
        if type(elem) == tuple:
            return UIActions.find_element(elem).text
        return elem.text

    @staticmethod
    @allure.step('Get element text.')
    def get_element_attribute_value(elem, attribute):
        if type(elem) == tuple:
            return UIActions.find_element(elem).get_attribute(attribute)
        return elem.get_attribute(attribute)

    @staticmethod
    @allure.step('Write text in input element.')
    def write_input_text(elem, text):
        if type(elem) == tuple:
            UIActions.find_element(elem).send_keys(text)
        else: elem.send_keys(text)

    @staticmethod
    @allure.step("eyes check window")
    def eyes_check_window(string):
        base.eyes.check_window(string)

    @staticmethod
    @allure.step("Get Element Text in List By index")
    def get_list_element_text_by_index(list, index):
        return list[index].text[:-7]

    @staticmethod
    @allure.step("Check if element displayed")
    def get_if_element_displayed(elem):
        return elem.is_displayed()
