import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from work_flows.web_flows import WebWorkFlow


class WebTests(WebWorkFlow):


    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://localhost:3000/")


    # @allure.title("Sign Up")
    # @allure.description("Sign up with new user and verify sign up succeeded")
    # def test_01(self):


