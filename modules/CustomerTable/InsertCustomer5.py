import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
sqlst = "INSERT INTO customer(account_number,name, balance) VALUES (%s, %s, %s)"
record1 = (1,"John",40)#INSERT ONE RECORD
mycursor.execute(sqlst, record1)
mydb.commit()