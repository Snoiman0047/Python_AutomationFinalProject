import allure
from main.page_objects.desktop.calculator_page import CalculatorPage
from main.page_objects.electron.demos_page import DemosPage
from main.page_objects.mobile.appium_page import appium_page
from main.page_objects.web.bank_accounts_page import BankAccounts
from main.page_objects.web.my_account_page import MyAccount
from main.page_objects.web.nav_bar_page import NavBar
from main.page_objects.web.profile_page import Profile
from main.page_objects.web.sign_in_page import SignIn
from main.page_objects.web.sign_up_page import SignUp
from main.utilities import base


class ManagePages:

    @staticmethod
    @allure.step('Initialization desktop pages.')
    def init_desktop_pages():
        base.calc_page = CalculatorPage()

    @staticmethod
    @allure.step('Initialization desktop pages.')
    def init_electron_pages():
        base.demos_page = DemosPage()

    @staticmethod
    @allure.step('Initialization web pages.')
    def init_web_pages():
        base.sign_up = SignUp(base.driver)
        base.sign_in = SignIn(base.driver)
        base.profile = Profile(base.driver)
        base.navbar = NavBar(base.driver)
        base.my_account = MyAccount(base.driver)
        base.bank_accounts = BankAccounts(base.driver)

    @staticmethod
    @allure.step("Initialization pages mobile.")
    def init_mobile_pages():
        base.app_page = appium_page()