from modules.Customerops import CustomerOps
from modules.Transactions import Transactions
from modules.Mysqlclass import DbOps


def atm():
    choice = int(input("Select options 1. add, 3. read"))
    if (choice == 1):
        details = cOps.addCustomer()
        cOps.firstDeposit(details)
    elif(choice == 2):
        rtn = txns.authCheck()
        if (rtn[0]):
            cOps.updateCustomer(rtn[1])
        else:
            print (rtn[1])
    elif(choice == 3):
        rtn = cOps.authCheck()
        if (rtn[0]):
            accountNumber = rtn[1][0]
            conditionData = {"condition":"account_number","value":accountNumber}
            cOps.readCustomer(conditionData)
        else:
            print (rtn[1])

DbOps.host = '127.0.0.1'
DbOps.port = 3307

database = 'bank'
password = 'pMac'
user = 'root'
txnTable = 'transactions'
cstmrTable = 'customers'

cOps = CustomerOps(database,password,user,cstmrTable)
txns = Transactions(database,password,user,txnTable)

# txns.depositMoney(1004)
txns.withdrawMoney(1004)
# txns.displayMoney(1004)

# atm()



