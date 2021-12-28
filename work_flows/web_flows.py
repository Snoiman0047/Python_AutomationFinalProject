import allure

from extensions.ui_actions import WebUiAction
from page_objects.web.sign_up_page import SignUp


class WebWorkFlow:
    sign_up = SignUp(driver)

    @allure.step("Sign up")
    def sign_up_user(self,first_name,last_name,user_name,password):
        WebUiAction.click_on(self.sign_up.Sign_Up_Link)
        WebUiAction.send_keys(self.sign_up.First_Name_Input,first_name)
        WebUiAction.send_keys(self.sign_up.Last_Name_Input, last_name)
        WebUiAction.send_keys(self.sign_up.User_Name_Input, user_name)
        WebUiAction.send_keys(self.sign_up.Password_Input, password)
        WebUiAction.send_keys(self.sign_up.ConfirmPassword_Input, password)
        WebUiAction.click_on(self.sign_up.SignUp_Btn)


