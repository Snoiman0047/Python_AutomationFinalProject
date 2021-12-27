import time
from applitools.selenium import Eyes

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from extensions.ui_actions import WebUiAction
from page_objects.web.bank_accounts_page import BankAccounts
from page_objects.web.my_account_page import MyAccount
from page_objects.web.nav_bar_page import NavBar
from page_objects.web.profile_page import Profile
from page_objects.web.sign_in_page import SignIn
from page_objects.web.sign_up_page import SignUp
from work_flows.web_flows import WebWorkFlow


class Tests_Web:

    def setup_class(cls):
        global driver, sign_up, sign_in, profile, navbar, my_account, action, eyes, bank_accounts
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://localhost:3000/")
        action = ActionChains(driver)
        eyes = Eyes()
        eyes.api_key = "1ERXihUFAuGZUWyCVGaVf1rUfXp1093i3iH0IbRdhlwos110"
        eyes.open(driver, "TestWeb", "My Account and Home")
        sign_up = SignUp(driver)
        sign_in = SignIn(driver)
        profile = Profile(driver)
        navbar = NavBar(driver)
        my_account = MyAccount(driver)
        bank_accounts = BankAccounts(driver)
        time.sleep(1)

    @allure.title("Sign Up")
    @allure.description("Sign up with new user and verify sign up succeeded")
    def test_01_sign_up(self):
        expected_title = "Sign in"
        sign_up.get_sign_up_link().click()
        sign_up.get_sign_up_link().click()
        sign_up.get_first_name_input().send_keys("Rami")
        sign_up.get_last_name_input().send_keys("Ghawi2")
        sign_up.get_user_name_input().send_keys("ramig")
        sign_up.get_password_input().send_keys("12345")
        sign_up.get_confirm_password_input().send_keys("12345")
        sign_up.get_sign_up_btn().click()
        time.sleep(1)

        assert sign_in.get_sign_in_title().text == expected_title

    @allure.title("Sign in")
    @allure.description("Sign in with exist user and verify sign in succeeded")
    def test_02_sign_in(self):
        expected_balance = "$1,681.37"
        sign_in.get_user_name_input().send_keys("Katharina_Bernier")
        sign_in.get_password_input().send_keys("s3cret")
        sign_in.get_sign_in_btn().click()
        time.sleep(1)
        eyes.check_window("Home page")

        assert profile.get_balance().text == expected_balance

    @allure.title("Update number in My Account")
    @allure.description("Update phone number and verify update succeeded")
    @pytest.mark.depends(on=['test_02_sign_in'])
    def test_03_update_phone_number(self):
        updated_phone_number = "050-550-0789"
        navbar.get_my_account_link().click()
        my_account.get_user_settings_phone_input().click()
        my_account.get_user_settings_phone_input().send_keys(Keys.CONTROL, 'a')
        my_account.get_user_settings_phone_input().send_keys(Keys.DELETE)
        my_account.get_user_settings_phone_input().send_keys(updated_phone_number)
        my_account.get_save_btn().click()

        assert my_account.get_user_settings_phone_input().get_attribute("value") == updated_phone_number

    @allure.title("Create Bank Account")
    @allure.description("Create bank account and verify create succeeded")
    @pytest.mark.depends(on=['test_02_sign_in'])
    def test_04_create_bank_account(self):
        navbar.get_bank_accounts_link().click()
        bank_accounts.get_create_btn().click()
        bank_accounts.get_bank_name_input().send_keys("TeamTen")
        bank_accounts.get_routing_number().send_keys("123456789")
        bank_accounts.get_account_number_input().send_keys("123456789")
        bank_accounts.get_save_btn().click()

        my_list = bank_accounts.get_accounts_list()

        assert self.step_get_list_bank_account_text(my_list, len(my_list) - 1)

    @allure.title("Home Page and Logout")
    @allure.description("Click on Home page + click on logout and verify logging out")
    @pytest.mark.depends(on=['test_02_sign_in'])
    def test_05_homepage_logout(self):
        navbar.get_home_link().click()
        eyes.check_window("After Click on Home")
        eyes.close()
        navbar.get_logout_link().click()
        time.sleep(1)

        assert sign_in.get_sign_in_title_after_logout().is_displayed()

    def teardown_class(self):
        driver.quit()
        eyes.abort()

    def step_get_list_bank_account_text(self, list, index):
        return list[index].text
