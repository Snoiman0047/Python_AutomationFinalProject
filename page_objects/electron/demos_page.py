import allure
from selenium.webdriver.common.by import By


class DemosPage:

    __BTN_CLIPBOARD_COPY_PASTE = (By.ID, 'button-clipboard')
    __INP_COPY = (By.ID, 'copy-to-input')
    __BTN_COPY = (By.ID, 'copy-to')

    @allure.step('Get copy-paste clipboard button.')
    def get_btn_clipboard_copy_paste(self):
        return self.__BTN_CLIPBOARD_COPY_PASTE

    @allure.step('Get copy input.')
    def get_copy_inp(self):
        return self.__INP_COPY

    @allure.step('Get copy button.')
    def get_btn_copy(self):
        return self.__BTN_COPY

