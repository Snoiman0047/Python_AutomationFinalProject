from selenium.webdriver.common.by import By


class Profile:

    def __init__(self, driver):
        self.driver = driver

    def get_balance(self):
        return self.driver.find_element(By.XPATH, '(//div[@class="MuiGrid-root MuiGrid-item"])[4]/h6[1]')