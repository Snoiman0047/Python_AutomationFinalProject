import unittest

import allure
import pytest
from extensions.ui_actions import UiAction
from work_flows.mobile_flows import mobile_work_flow
from extensions.db_actions import DBAction as db

@pytest.mark.usefixtures('init_mobile')
class Test_Case:
    @allure.title('Test01')
    @allure.description('loan calculator and verify monthly payment')
    def test_01(self):
        mobile_work_flow.loan_calc(db.get_details()[5][0],db.get_details()[6][0],db.get_details()[7][0]
                                   ,db.get_details()[8][0],db.get_details()[9][0])
        res = mobile_work_flow.monthly_payment()
        UiAction.verify_test(res,db.get_details()[0][0])

    @allure.title('Test02')
    @allure.description('verify total payment')
    def test_02(self):
        res = mobile_work_flow.total_payment()
        UiAction.verify_test(res, db.get_details()[1][0])

    @allure.title('Test03')
    @allure.description('verify total interest')
    def test_03(self):
        res = mobile_work_flow.total_interest()
        UiAction.verify_test(res, db.get_details()[2][0])

    @allure.title('Test04')
    @allure.description('verify interest saving')
    def test_04(self):
        res = mobile_work_flow.interest_saving()
        UiAction.verify_test(res,db.get_details()[4][0])


