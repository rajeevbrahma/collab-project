#Creating Database Table
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
#mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customer(account_number INTEGER , name VARCHAR(50),balance INTEGER(10))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
 print(x)