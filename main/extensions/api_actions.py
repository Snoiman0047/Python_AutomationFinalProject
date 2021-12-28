import allure
import requests


class ApiActions:
    @staticmethod
    @allure.step("Post Action")
    def post_action(dictionary: dict, url):
        response = requests.post(url, data=dictionary)
        return response

    @staticmethod
    @allure.step("Patch Action")
    def patch_action(dictionary: dict, url):
        response = requests.patch(url, data=dictionary)
        return response

    @staticmethod
    @allure.step("Delete Action")
    def delete_action(url):
        response = requests.delete(url)
        return response
