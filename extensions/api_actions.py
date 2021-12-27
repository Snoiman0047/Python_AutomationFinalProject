import json
import allure
import requests


class Api_Actions:
    @staticmethod
    @allure.step("Post Action")
    def post_action(dictionary: dict, url):
        response = requests.post(url, data=dictionary)
        response_json = response.json()
        print("POST Response Body:", json.dumps(response_json, indent=2))
        return response

    @staticmethod
    @allure.step("Patch Action")
    def patch_action(dictionary: dict, url):
        response = requests.patch(url, data=dictionary)
        response_json = response.json()
        print("PATCH Response Body:", json.dumps(response_json, indent=2))
        return response

    @staticmethod
    @allure.step("Delete Action")
    def delete_action(url):
        response = requests.delete(url)
        response_json = response.json()
        print("DELETE Response Body:", json.dumps(response_json, indent=2)) #will be empty
        return response


    @staticmethod
    @allure.step("Verify Status Code Action")
    def verify_status_code_action(status_code, expected_result):
        assert status_code == expected_result