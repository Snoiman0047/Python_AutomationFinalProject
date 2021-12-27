import allure


class WebUiAction:

    @allure.step("Click on an element")
    def click_on(self, elem):
        elem.click()

    @allure.step("Send keys to Input")
    def send_keys(self, elem, input):
        elem.send_keys(input)

    @allure.step("Element Text")
    def get_text(self, elem):
        elem.text