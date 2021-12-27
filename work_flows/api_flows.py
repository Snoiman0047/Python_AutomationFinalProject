import allure
from extensions.api_actions import Api_Actions


class Api_Flows:
    @staticmethod
    @allure.step("Post Flow")
    def post_flows(dictionary: dict, url):
        return Api_Actions.post_action(dictionary, url)

    @staticmethod
    @allure.step("Patch Flow")
    def patch_flows(dictionary: dict, url):
        return Api_Actions.patch_action(dictionary, url)

    @staticmethod
    @allure.step("Delete Flow")
    def delete_flows(url):
        return Api_Actions.delete_action(url)

    @staticmethod
    @allure.step("Verify Status Code Flow")
    def verify_status_code_flow(status_code, expected_result):
        return Api_Actions.verify_status_code_action(status_code, expected_result)
