import allure

from extensions.ui_actions import UI_actions
from extensions.verifications import Verifications
from utilities import base
from utilities.managers.manage_ddt import get_data


class DemosFlow:

    @staticmethod
    @allure.step('Copy paste text.')
    def copy_action(text):
        UI_actions.click(base.demos_page.get_btn_clipboard_copy_paste())
        UI_actions.write_input_text(base.demos_page.get_copy_inp(), text)
        UI_actions.click(base.demos_page.get_btn_copy())

    @staticmethod
    @allure.step('Copy-paste action verification.')
    def verify_copy_action():
        Verifications.string_value(UI_actions.get_element_attribute_value(base.demos_page.get_copy_inp(), 'placeholder')
                                   , get_data('COPY_RESULT_TEXT'), 'The copy-paste action did not work as expected.')