import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import IEDriverManager

from utilities import base
from utilities.listeners import EventListener
from utilities.managers.manage_db import ManageDb
from utilities.managers.manage_ddt import get_data
from utilities.managers.manage_pages import ManagePages


@pytest.fixture(scope='class')
@allure.step('Desktop app identification.')
def init_desktop(request):
    globals()['platform_name'] = 'desktop'
    globals()['desired_caps'] = {'app': get_data('APP'), 'platformName': get_data('PLATFORM_NAME'),
                                 'deviceName': get_data('DEVICE_NAME')}
    globals()['driver'] = webdriver.Remote('http://127.0.0.1:4723', globals()['desired_caps'])
    request.cls.driver = globals()['driver']
    globals()['driver'].implicitly_wait(5)
    ManagePages.init_desktop_pages()
    yield
    globals()['driver'].quit()

@pytest.fixture(scope='class')
def init_mobile(request):
    base.platform_name = 'mobile'
    desired_caps = {"udid": get_data('UDID'), "appPackage": get_data('APP_PACKAGE'),
                                 "appActivity":get_data('APP_ACTIVITY'), "platformName":get_data('PLATFORM_NAME_ANDROID')}
    base.driver = webdriver.Remote(get_data('URL_MOBLIE'), desired_caps)
    ManageDb.connect_Db()
    base.driver.implicitly_wait(5)
    ManagePages.init_mobile_pages()
    yield
    base.driver.quit()






@pytest.fixture(scope='class')
@allure.step('Web browser identification.')
def init_web(request):
    # browser_type = os.getenv('BrowserType')
    browser_type = get_data('BrowserType')
    globals()['driver'] = EventFiringWebDriver(get_initialized_driver(browser_type), EventListener())
    request.cls.driver = globals()['driver']
    globals()['driver'].maximize_window()
    yield
    globals()['driver'].quit()


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
