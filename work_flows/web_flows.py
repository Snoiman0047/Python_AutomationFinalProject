import allure

from extensions.ui_actions import WebUiAction
from page_objects.web.sign_up_page import SignUp


class WebWorkFlow():

    @allure.step("Sign up")
    def sign_up_user(self,first_name, last_name, user_name, password):
        WebUiAction.click_on(SignUp.get_sign_up_link(self))
        WebUiAction.send_keys(SignUp.get_first_name_input(SignUp()), first_name)
        WebUiAction.send_keys(SignUp.get_last_name_input(), last_name)
        WebUiAction.send_keys(SignUp.get_user_name_input(), user_name)
        WebUiAction.send_keys(SignUp.get_password_input(), password)
        WebUiAction.send_keys(SignUp.get_confirm_password_input(), password)
        WebUiAction.click_on(SignUp.get_sign_up_btn())
