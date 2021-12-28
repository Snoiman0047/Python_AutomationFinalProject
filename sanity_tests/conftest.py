import time

import allure
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import IEDriverManager
from utilities import base
from utilities.listeners import EventListener
from utilities.managers.manage_ddt import get_data
from utilities.managers.manage_pages import ManagePages


@pytest.fixture(scope='class')
# @allure.step('Desktop app identification.')
def init_desktop(request):
    print("Nisionnnnnnnnn")
    desired_caps = {}
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_caps["platformName"] = "Windows"
    desired_caps["deviceName"] = "WindowsPC"
    base.driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
    base.driver.implicitly_wait(5)
    ManagePages.init_desktop_pages()

    yield
    base.driver.quit()


@pytest.fixture(scope='class')
# @allure.step('Web browser identification.')
def init_web(request):
    base.driver = webdriver.Chrome(ChromeDriverManager().install())
    base.driver.maximize_window()
    base.driver.get("http://localhost:3000/")
    base.action = ActionChains(base.driver)
    init_eyes()
    ManagePages.init_web_pages()
    # browser_type = os.getenv('BrowserType')
    # browser_type = get_data('BrowserType')
    # base.driver = EventFiringWebDriver(get_initialized_driver(browser_type), EventListener())

    yield
    base.driver.quit()
    base.eyes.abort()


@allure.step('Chrome driver initialization.')
def init_chrome_driver():
    _driver = webdriver.Chrome(ChromeDriverManager().install())
    return _driver


@allure.step('Internet Explorer driver initialization.')
def init_ie_driver():
    _driver = webdriver.Ie(IEDriverManager().install())
    return _driver


@allure.step('Opera driver initialization.')
def init_opera_driver():
    _driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    return _driver


@allure.step('Firefox driver initialization.')
def init_ff_driver():
    _driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return _driver


@allure.step('Edge driver initialization.')
def init_edge_driver():
    _driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return _driver


@allure.step('Initialize driver by browser type.')
def get_initialized_driver(browser_type):
    if browser_type.lower() == 'chrome':
        return init_chrome_driver()
    elif browser_type.lower() == 'edge':
        return init_edge_driver()
    elif browser_type.lower() == 'firefox':
        return init_ff_driver()
    elif browser_type.lower() == 'opera':
        return init_opera_driver()
    elif browser_type.lower() == 'ie':
        return init_ie_driver()
    else:
        raise Exception('Unrecognized browser')


@allure.step("Init and open Eyes")
def init_eyes():
    base.eyes = Eyes()
    base.eyes.api_key = get_data("EyesAPIKey")
    base.eyes.open(base.driver, get_data("EyesApplitoolsTitle"), get_data("EyesApplitoolsSubTitle"))
