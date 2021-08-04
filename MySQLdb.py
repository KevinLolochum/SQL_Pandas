import mysql.connector as mysql
import csv
import datetime

transactions = mysql.connect(
    host = 'localhost',
    user = 'root',
    # Forces connection to use native plugin incase of error
    auth_plugin='mysql_native_password', 
    password = 'password',
    database = "db")

cursor = transactions.cursor()

cursor.execute("select database();")

# To fetch only one case of the database
record = cursor.fetchone()

cursor.execute('DROP TABLE IF EXISTS table_name;')

cursor.execute("CREATE TABLE table_name(transaction_id varchar(255), \
transaction_date varchar(255),product_name varchar(255),price varchar(255),store_name varchar(255), \
sales_representative_name varchar(255), client_name varchar(255))")

with open('transactions_csv.csv', 'r') as file:
    next(file) # To skip the first line
    data = csv.reader(file, dialect = 'excel')
    for row in data:
        date_format = '%m/%d/%Y'
        DML = """INSERT INTO db.table_name
            VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(DML, row)


        
transactions.commit()
transactions.close

print('Complete')
