#Creating Database Table
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
"""mycursor.execute("show databases")
for x in mycursor:
  print(x)"""

mycursor.execute("show tables")
for x in mycursor:
  print(x)

#mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
mycursor.execute("SHOW TABLES")
for x in mycursor:
 print(x)