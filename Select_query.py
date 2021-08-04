import mysql.connector as mysql
import csv
transactions = mysql.connect(
    host = 'localhost',
    user = 'root',
    # Forces connection to use native plugin incase of error
    auth_plugin='mysql_native_password', 
    password = 'pasword',
    database = "db")

cursor = transactions.cursor()

cursor.execute("select database();")

# Fetch database
record = cursor.fetchone()





Select = "select * from db.table"

cursor.execute(Select)

#fecth all records
Output = cursor.fetchall()

for i in Output:
    print(i)

transactions.commit()
