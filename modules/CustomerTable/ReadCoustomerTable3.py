#readtable (customer)
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root@123",
database="python_bank"
)
mycursor = mydb.cursor()
#PULL DATA FROM THE TABLE
mycursor.execute("SELECT * FROM customer")
result = mycursor.fetchall()
print("account_number\t\tname\t\tbalance")
print("-----\t\t\t---\t\t---")
for row in result:
    print("\t""%s" %row[0] + "\t\t%s" %row[1] + "\t\t%s" %row[2])

