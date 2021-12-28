from selenium.webdriver.common.by import By


class NavBar:

    def __init__(self, driver):
        self.driver = driver

    def get_home_link(self):
        return self.driver.find_element(By.XPATH, '//ul[@class="MuiList-root MuiList-padding"]/div/a[1]')

    def get_my_account_link(self):
        return self.driver.find_element(By.XPATH,'//ul[@class="MuiList-root MuiList-padding"]/div/a[2]')

    def get_logout_link(self):
        return self.driver.find_element(By.XPATH, '//ul[@class="MuiList-root MuiList-padding"]/div/div')

    def get_bank_accounts_link(self):
        return self.driver.find_element(By.XPATH, '//ul[@class="MuiList-root MuiList-padding"]/div/a[3]')