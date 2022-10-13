"""
    display money
    deposit money
    withdraw money

"""

from modules.Mysqlclass import DbOps

class Transactions(DbOps):
    def __init__(self,database,password,user,table):
        DbOps.__init__(self,database,password,user,table) 
        self.connect()
        self.fetchDbVersion()
        print ("Connected to Transactions DATABASE")


    def displayMoney(self,accountNumber):
        conditionData = {"condition":"account_number","value":accountNumber}
        result = self.readById(conditionData)
        print (f" {accountNumber}'s Balance = {result[2]}")

    def depositMoney(self,accountNumber):
        deposit_amount = int(input("Deposit amount : "))
        conditionData = {"condition":"account_number","value":accountNumber}
        doc = self.readById(conditionData)
        data = [("balance",doc[2]+deposit_amount)]
        self.update(conditionData,data)
            
    def withdrawMoney(self,accountNumber):
        withdraw_amount = int(input("Withdraw amount : "))
        conditionData = {"condition":"account_number","value":accountNumber}
        doc = self.readById(conditionData)
        if (withdraw_amount < doc[2]):
            data = [("balance",doc[2]-withdraw_amount)]
            self.update(conditionData,data)
        else:
            print ("Insufficient Funds !!!")     

    def firstDeposit(self,details):
        deposit = input(" Add your initial deposit .. ")
        self.create(
                        [
                            "account_number",
                            "name",
                            "balance",
                            "account_pin",
                        ],
                        [
                            details[0],
                            "'"+details[1]+"'",
                            deposit,
                            details[2] 
                        ]
                        )
        