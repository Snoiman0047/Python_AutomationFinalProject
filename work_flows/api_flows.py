import allure
from extensions.api_actions import ApiActions


class ApiFlows:
    @staticmethod
    @allure.step("Post Flow")
    def post_flows(dictionary: dict, url):
        return ApiActions.post_action(dictionary, url)

    @staticmethod
    @allure.step("Patch Flow")
    def patch_flows(dictionary: dict, url):
        return ApiActions.patch_action(dictionary, url)

    @staticmethod
    @allure.step("Delete Flow")
    def delete_flows(url):
        return ApiActions.delete_action(url)
