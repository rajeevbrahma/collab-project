import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
my_sql = "UPDATE customer SET balance = 80 WHERE account_number = 2"
mycursor.execute(my_sql)
mydb.commit()