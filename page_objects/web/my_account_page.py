from selenium.webdriver.common.by import By


class MyAccount:

    def __init__(self, driver):
        self.driver = driver

    def get_user_settings_phone_input(self):
        return self.driver.find_element(By.ID, 'user-settings-phoneNumber-input')

    def get_save_btn(self):
        return self.driver.find_element(By.XPATH, '//div[@class="MuiGrid-root MuiGrid-item"]//button')
