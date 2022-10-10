#insert many records
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
#INSERT MULTIPLE RECORDS
sqlst = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [("Paul", "Paul@Paul.com", 32),
("Ben", "Ben@Ben.com", 21),
("Harsha", "Harsha@HarshaEmail.com", 30),
("Joe", "joe@joejoe.com", 60),]
mycursor.executemany(sqlst, records)
mydb.commit()