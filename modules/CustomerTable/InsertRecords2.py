#insert many records
import mysql.connector
# Localhost IP 127.0.0.1
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
#INSERT MULTIPLE RECORDS
sqlst = "INSERT INTO customer (account_number,name,balance) VALUES (%s, %s, %s)"
records = [(2,"Paul", 70),
(3,"Ben", 70),
(4,"Harsha", 70 ),
(5,"Joe", 70),]
mycursor.executemany(sqlst, records)
mydb.commit()