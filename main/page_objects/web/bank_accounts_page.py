from selenium.webdriver.common.by import By


class BankAccounts:

    def __init__(self, driver):
        self.driver = driver

    def get_create_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item']/a")

    def get_bank_name_input(self):
        return self.driver.find_element(By.ID, 'bankaccount-bankName-input')

    def get_routing_number(self):
        return self.driver.find_element(By.ID, 'bankaccount-routingNumber-input')

    def get_account_number_input(self):
        return self.driver.find_element(By.ID, 'bankaccount-accountNumber-input')

    def get_save_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item']/button")

    def get_accounts_list(self):
        return self.driver.find_elements(By.XPATH, '//ul[@class="MuiList-root MuiList-padding"]//li')
