import allure
import pytest
from main.extensions.verifications import Verifications
from main.work_flows import mobile_work_flow
from main.extensions.db_actions import DBAction as db


@pytest.mark.usefixtures('init_mobile')
class Test_Case:
    @allure.title('Test01')
    @allure.description('loan calculator and verify monthly payment')
    def test_01(self):
        mobile_work_flow.loan_calc(db.get_details()[5][0],db.get_details()[6][0],db.get_details()[7][0]
                                   ,db.get_details()[8][0],db.get_details()[9][0])
        res = mobile_work_flow.monthly_payment()
        Verifications.verify_equals(res, db.get_details()[0][0], 'Unexpected result.')

    @allure.title('Test02')
    @allure.description('verify total payment')
    def test_02(self):
        res = mobile_work_flow.total_payment()
        Verifications.verify_equals(res, db.get_details()[1][0], 'Unexpected result.')

    @allure.title('Test03')
    @allure.description('verify total interest')
    def test_03(self):
        res = mobile_work_flow.total_interest()
        Verifications.verify_equals(res, db.get_details()[2][0], 'Unexpected result.')

    @allure.title('Test04')
    @allure.description('verify interest saving')
    def test_04(self):
        res = mobile_work_flow.interest_saving()
        Verifications.verify_equals(res,db.get_details()[4][0], 'Unexpected result.')


