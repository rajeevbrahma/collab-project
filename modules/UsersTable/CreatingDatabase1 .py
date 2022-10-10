#connecting DATABASE
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123"
)
print(mydb)
"""
Cursor is a Temporary Memory or Temporary Work Station.
 It is Allocated by Database Server at the Time of Performing DML(Data Manipulation Language) 
 operations on Table by User. Cursors are used to store Database Tables
"""

mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE projDj")
mycursor.execute("SHOW DATABASES")
print(type(mycursor))
for db in mycursor:
    print(db)