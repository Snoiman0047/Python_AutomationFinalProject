import mysql.connector
global mydb
mydb = mysql.connector.connect(
            host="remotemysql.com",
            database="e7qIjyMgHh",
            user="e7qIjyMgHh",
            password="ALKcxfmtTt"
        )

query = "SELECT value FROM Test_values"
my_cursor = mydb.cursor()
my_cursor.execute(query)
my_result = my_cursor.fetchall()
#print(my_result[1][0])