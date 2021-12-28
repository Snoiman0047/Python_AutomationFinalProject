import allure
import mysql.connector
from main.utilities import base
from main.utilities.manage_ddt import get_data


class ManageDb:
    @staticmethod
    @allure.step('Connect to Db.')
    def connect_Db():
        base.mydb = mysql.connector.connect(
            host=get_data('HOST'),
            database=get_data('DB'),
            user=get_data('USER'),
            password=get_data('PASS')
        )

    @staticmethod
    @allure.step('Close Db connection.')
    def teardown_class():
        base.mydb.close()
