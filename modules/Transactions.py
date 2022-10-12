"""
    display money
    deposit money
    withdraw money

"""

from Mysqlclass import DbOps

class CustomerOps(DbOps):
    def __init__(self,database,password,user,table):
        DbOps.__init__(self,database,password,user,table) 
        self.connect()
        self.fetchDbVersion()

    def authCheck(self):
        account_number = int(input("Enter account number"))
        docs = self.read()
        for doc in docs :
            if account_number in doc:
                name = doc[1]
                print (f"Welcome {name} ....")
                password = input("Enter password")
                if password == doc[3]:
                    return True,doc
                else:
                    return False,"Wrong password"
            else:
                return False,"Account not found"

    def displayMoney(self):
        checkReturn,doc = self.authCheck()
        if (checkReturn):
            print (doc[2]) 

    def depositMoney(self):
        checkReturn,doc = self.authCheck()
        deposit_amount = int(input("Deposit amount : "))
        if (checkReturn):
            self.update({"account_number":doc[0]},{"balance":deposit_amount})
            

    def withdrawMoney(self):
        checkReturn,doc = self.authCheck()
        withdraw_amount = int(input("Withdraw amount : "))
        if (checkReturn):
            self.update({"account_number":doc[0]},{"balance":withdraw_amount})
             

DbOps.host = '127.0.0.1'
DbOps.port = 3307

database = 'bank'
password = 'pMac'
user = 'root'
table = 'transactions'

