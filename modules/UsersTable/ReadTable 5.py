#readtable (users)
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
#PULL DATA FROM THE TABLE
mycursor.execute("SELECT * FROM users")
result = mycursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
    print(row[0] + "\t""%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

