import allure
from utilities import base

class DBAction:
    @staticmethod
    @allure.step("get all details From the db")
    def get_details():
        query = "SELECT value FROM Test_values"
        my_cursor = base.mydb.cursor()
        my_cursor.execute(query)
        return my_cursor.fetchall()

