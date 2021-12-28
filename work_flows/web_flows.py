import time

import allure
from selenium.webdriver.common.keys import Keys

from extensions.ui_actions import UI_Actions
from utilities import base


class WebWorkFlow:

    @staticmethod
    @allure.step("Sign up")
    def sign_up_user(first_name, last_name, user_name, password):
        UI_Actions.click(base.sign_up.get_sign_up_link())
        UI_Actions.click(base.sign_up.get_sign_up_link())
        UI_Actions.send_keys(base.sign_up.get_first_name_input(), first_name)
        UI_Actions.send_keys(base.sign_up.get_last_name_input(), last_name)
        UI_Actions.send_keys(base.sign_up.get_user_name_input(), user_name)
        UI_Actions.send_keys(base.sign_up.get_password_input(), password)
        UI_Actions.send_keys(base.sign_up.get_confirm_password_input(), password)
        UI_Actions.click(base.sign_up.get_sign_up_btn())
        time.sleep(1)

    @staticmethod
    @allure.step("Sign in Title")
    def step_get_sign_in_title():
        return UI_Actions.get_element_text(base.sign_in.get_sign_in_title())

    @staticmethod
    @allure.step("Sign in")
    def sign_in(username, password):
        UI_Actions.send_keys(base.sign_in.get_user_name_input(), username)
        UI_Actions.send_keys(base.sign_in.get_password_input(), password)
        UI_Actions.click(base.sign_in.get_sign_in_btn())
        time.sleep(1)

    @staticmethod
    @allure.step("Home page check window")
    def check_home_page_window(string):
        UI_Actions.eyes_check_window(string)

    @staticmethod
    @allure.step("Balance")
    def step_get_balance_text():
        return UI_Actions.get_element_text(base.profile.get_balance())

    @staticmethod
    @allure.step("Update Phone Number")
    def update_phone_number(new_phone_number):
        UI_Actions.click(base.navbar.get_my_account_link())
        UI_Actions.click(base.my_account.get_user_settings_phone_input())
        UI_Actions.send_keys(base.my_account.get_user_settings_phone_input(), (Keys.CONTROL, 'a'))
        UI_Actions.send_keys(base.my_account.get_user_settings_phone_input(), Keys.DELETE)
        UI_Actions.send_keys(base.my_account.get_user_settings_phone_input(), new_phone_number)
        UI_Actions.click(base.my_account.get_save_btn())

    @staticmethod
    @allure.step("User phone input value")
    def step_get_user_phone_input_attribute_value():
        return UI_Actions.get_attribute_value(base.my_account.get_user_settings_phone_input())

    @staticmethod
    @allure.step("Create Bank Account")
    def create_bank_account(bank_name, routing_number, account_number):
        UI_Actions.click(base.navbar.get_bank_accounts_link())
        UI_Actions.click(base.bank_accounts.get_create_btn())
        UI_Actions.send_keys(base.bank_accounts.get_bank_name_input(), bank_name)
        UI_Actions.send_keys(base.bank_accounts.get_routing_number(), routing_number)
        UI_Actions.send_keys(base.bank_accounts.get_account_number_input(), account_number)
        UI_Actions.click(base.bank_accounts.get_save_btn())

    @staticmethod
    @allure.step("User phone input value")
    def step_get_last_created_account_text():
        my_list = base.bank_accounts.get_accounts_list()
        return UI_Actions.get_list_element_text_by_index(my_list, len(my_list) - 1)

    @staticmethod
    @allure.step("Get Home Page")
    def navigate_to_home_page():
        UI_Actions.click(base.navbar.get_home_link())

    @staticmethod
    @allure.step("Logout")
    def logout_user():
        UI_Actions.click(base.navbar.get_logout_link())
        time.sleep(1)

    @staticmethod
    @allure.step("Close Eyes")
    def close_eyes():
        base.eyes.close()

    @staticmethod
    @allure.step("Sign in title")
    def check_if_title_displayed():
        UI_Actions.get_if_element_displayed(base.sign_in.get_sign_in_title_after_logout())


