from selenium.webdriver.common.by import By


class SignUp:

    def __init__(self, driver):
        self.driver = driver

    def get_sign_up_link(self):
        return self.driver.find_element(By.XPATH, '//div[2]/a')

    def get_first_name_input(self):
        return self.driver.find_element(By.ID, 'firstName')

    def get_last_name_input(self):
        return self.driver.find_element(By.ID, 'lastName')

    def get_user_name_input(self):
        return self.driver.find_element(By.ID, 'username')

    def get_password_input(self):
        return self.driver.find_element(By.ID, 'password')

    def get_confirm_password_input(self):
        return self.driver.find_element(By.ID, 'confirmPassword')

    def get_sign_up_btn(self):
        return self.driver.find_element(By.XPATH, '//form/button/span[1]')




