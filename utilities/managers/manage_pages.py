import allure
from page_objects.desktop.calculator_page import CalculatorPage
from page_objects.web.bank_accounts_page import BankAccounts
from page_objects.web.my_account_page import MyAccount
from page_objects.web.nav_bar_page import NavBar
from page_objects.web.profile_page import Profile
from page_objects.web.sign_in_page import SignIn
from page_objects.web.sign_up_page import SignUp
from utilities import base


class ManagePages:

    @staticmethod
    @allure.step("Initialization desktop pages.")
    def init_desktop_pages():
        base.calc_page = CalculatorPage(base.driver)

    @staticmethod
    @allure.step("Initialization web pages.")
    def init_web_pages():
        base.calc_page = CalculatorPage(base.driver)
        base.sign_up = SignUp(base.driver)
        base.sign_in = SignIn(base.driver)
        base.profile = Profile(base.driver)
        base.navbar = NavBar(base.driver)
        base.my_account = MyAccount(base.driver)
        base.bank_accounts = BankAccounts(base.driver)
