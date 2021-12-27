from selenium.webdriver.common.by import By


class SignUp:

    def __init__(self, driver):
        self.driver = driver

    Sign_Up_Link = (By.XPATH, '//div[2]/a')

    First_Name_Input = (By.ID, 'firstName')

    Last_Name_Input = (By.ID, 'lastName')

    User_Name_Input = (By.ID, 'username')

    Password_Input = (By.ID, 'password')

    ConfirmPassword_Input = (By.ID, 'confirmPassword')

    SignUp_Btn = (By.XPATH, '//form/button/span[1]')


