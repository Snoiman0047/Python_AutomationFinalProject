import allure

from work_flows.api_flows import Api_Flows

url = "http://localhost:3000"
header = {"Content-type": "application/json"}
string_resource = "/posts"
test_id = "/101"
payload = {}


class Test_API_JSON_Server:
    # 1 - POST
    @allure.title("Test Verify Post")
    @allure.description("This Test Verifying A Post Was Created")
    def test_01_post(self):
        payload = {'userId': '11', 'id': '101', 'title': 'Team10', 'body': 'POST Test'}
        status_code = Api_Flows.post_flows(payload, url + string_resource).status_code
        Api_Flows.verify_status_code_flow(status_code, 201)

    # 2 - PATCH
    @allure.title("Test Verify Patch")
    @allure.description("This Test Verifying A Post Was Edited")
    def test_02_patch(self):
        payload = {'title': 'Team10Edit', 'body': 'PATCH Test'}
        status_code = Api_Flows.patch_flows(payload, url + string_resource + test_id).status_code
        Api_Flows.verify_status_code_flow(status_code, 200)

    # 3 - DELETE
    @allure.title("Test Verify Delete")
    @allure.description("This Test Verifying A Post Was Deleted")
    def test_03_delete(self):
        status_code = Api_Flows.delete_flows(url + string_resource + test_id).status_code
        Api_Flows.verify_status_code_flow(status_code, 200)
