#Insert Operation
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
sqlst= "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)#INSERT ONE RECORD
mycursor.execute(sqlst, record1)
mydb.commit()