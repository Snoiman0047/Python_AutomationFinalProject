import allure
from extensions.verifications import Verifications
from utilities.managers.manage_ddt import get_data
from work_flows.api_flows import ApiFlows
from utilities import base


class TestAPIJSONServer:
    # 1 - POST
    @allure.title("Test Verify Post")
    @allure.description("This Test Verifying A Post Was Created")
    def test_01_post(self):
        base.payload = {'userId': get_data("New_Value_User_Id"), 'id': get_data("New_Value_Id"), 'title': get_data("New_Value_Title"), 'body': get_data("New_Value_Body")}
        base.status_code = ApiFlows.post_flows(base.payload, get_data("API_URL") + get_data("String_Resource")).status_code
        Verifications.string_value(base.status_code, 201, "Status code is different")

    # 2 - PATCH
    @allure.title("Test Verify Patch")
    @allure.description("This Test Verifying A Post Was Edited")
    def test_02_patch(self):
        base.payload = {'title': get_data("Edit_Value_Title"), 'body': get_data("Edit_Value_Body")}
        base.status_code = ApiFlows.patch_flows(base.payload, get_data("API_URL") + get_data("String_Resource") + get_data("Test_Id")).status_code
        Verifications.string_value(base.status_code, 200, "Status code is different")

    # 3 - DELETE
    @allure.title("Test Verify Delete")
    @allure.description("This Test Verifying A Post Was Deleted")
    def test_03_delete(self):
        base.status_code = ApiFlows.delete_flows(get_data("API_URL") + get_data("String_Resource") + get_data("Test_Id")).status_code
        Verifications.string_value(base.status_code, 200, "Status code is different")
