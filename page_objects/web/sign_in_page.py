from selenium.webdriver.common.by import By


class SignIn:

    def __init__(self, driver):
        self.driver = driver

    def get_sign_in_title(self):
        return self.driver.find_element(By.XPATH, "//div[@class='makeStyles-paper-21']//h1")

    def get_sign_in_title_after_logout(self):
        return self.driver.find_element(By.XPATH, '//h1[@class="MuiTypography-root MuiTypography-h5"]')

    def get_user_name_input(self):
        return self.driver.find_element(By.ID, 'username')

    def get_password_input(self):
        return self.driver.find_element(By.ID, 'password')

    def get_sign_in_btn(self):
        return self.driver.find_element(By.XPATH, '//span[@class="MuiButton-label"]')
