import allure
import pytest

from extensions.verifications import Verifications
from utilities import base
from utilities.managers.manage_ddt import get_data
from work_flows.web_flows import WebWorkFlow


@pytest.mark.usefixtures("init_web")
class Tests_Web:

    @allure.title("Sign Up")
    @allure.description("Sign up with new user and verify sign up succeeded")
    def test_01_sign_up(self):
        WebWorkFlow.sign_up_user(get_data("NewFirstName"), get_data("NewLastName"), get_data("NewUserName"), get_data("NewPassword"))

        Verifications.verify_equals(WebWorkFlow.step_get_sign_in_title(), get_data("ExpectedSignInTitle"), get_data("MessageTest1"))

    @allure.title("Sign in")
    @allure.description("Sign in with exist user and verify sign in succeeded")
    def test_02_sign_in(self):
        WebWorkFlow.sign_in(get_data("UserName"), get_data("PassWord"))
        WebWorkFlow.check_home_page_window(get_data("CheckWindowBase"))

        Verifications.verify_equals(WebWorkFlow.step_get_balance_text(), get_data("ExpectedBalance"), get_data("MessageTest2"))

    @allure.title("Update number in My Account")
    @allure.description("Update phone number and verify update succeeded")
    @pytest.mark.depends(on=['test_02_sign_in'])
    def test_03_update_phone_number(self):
        WebWorkFlow.update_phone_number(get_data("NewPhoneNumber"))

        Verifications.verify_equals(WebWorkFlow.step_get_user_phone_input_attribute_value(), get_data("NewPhoneNumber"), get_data("MessageTest3"))

    @allure.title("Create Bank Account")
    @allure.description("Create bank account and verify create succeeded")
    @pytest.mark.depends(on=['test_02_sign_in'])
    def test_04_create_bank_account(self):
        WebWorkFlow.create_bank_account(get_data("NewAccountName"), get_data("NewRoutingNumber"), get_data("NewAccountNumber"))

        Verifications.verify_equals(WebWorkFlow.step_get_last_created_account_text(), get_data("NewAccountName"),
                                    get_data("MessageTest4"))

    @allure.title("Home Page and Logout")
    @allure.description("Click on Home page + click on logout and verify logging out")
    @pytest.mark.depends(on=['test_02_sign_in'])
    def test_05_homepage_logout(self):
        WebWorkFlow.navigate_to_home_page()
        WebWorkFlow.check_home_page_window(get_data("CheckWindowAfter"))
        WebWorkFlow.close_eyes()
        WebWorkFlow.logout_user()

        Verifications.verify_true(WebWorkFlow.check_if_title_displayed(), get_data("MessageTest5"))



