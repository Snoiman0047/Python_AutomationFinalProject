import allure
import mysql.connector
from utilities import base

class ManageDb:
    @staticmethod
    @allure.step("connect Db")
    def connect_Db():
        base.mydb = mysql.connector.connect(
            host="remotemysql.com",
            database="e7qIjyMgHh",
            user="e7qIjyMgHh",
            password="ALKcxfmtTt"
        )

    @staticmethod
    @allure.step("close Db")
    def teardown_class(cls):
        base.mydb.close()
