import allure


class WebUiAction:
    @staticmethod
    @allure.step("Click on an element")
    def click_on(elem):
        elem.click()

    @staticmethod
    @allure.step("Send keys to Input")
    def send_keys(elem, input):
        elem.send_keys(input)

    @staticmethod
    @allure.step("Element Text")
    def get_text(elem):
        elem.text