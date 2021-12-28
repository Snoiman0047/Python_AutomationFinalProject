import allure
import mysql.connector
from utilities import base
from utilities.managers.manage_ddt import get_data


class ManageDb:
    @staticmethod
    @allure.step("connect Db")
    def connect_Db():
        base.mydb = mysql.connector.connect(
            host=get_data('HOST'),
            database=get_data('DB'),
            user=get_data('USER'),
            password=get_data('PASS')
        )

    @staticmethod
    @allure.step("close Db")
    def teardown_class():
        base.mydb.close()
