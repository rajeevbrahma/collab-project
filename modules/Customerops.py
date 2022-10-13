"""

    add customer
    update customer
    read customer
    delete customer

"""

from modules.Mysqlclass import DbOps
import datetime

class CustomerOps(DbOps):
    
    customerNumber = 0

    def __init__(self,database,password,user,table):
        DbOps.__init__(self,database,password,user,table) 
        self.connect()
        self.fetchDbVersion()
        self.getAccountNumber()
        print ("Connected to Customers DATABASE") 

    def getAccountNumber(self):
        docs = self.read()
        accountNumbers = []
        for doc in docs:
            accountNumbers.append(doc[0])
        CustomerOps.customerNumber = max(accountNumbers) + 1

    def customer_info_validation(self,pincode=None,ssn=None,dob=None,name=None,password=None):
    
        if name != None:
            for symbol in ["_",",",".","1","2","3","4","5","6","7","8","9","0"]:
                if (symbol in name):
                    return False,"Name contains symbol or number"
        
        if ssn != None and len(ssn) != 4:
            return False,"invalid ssn"

        elif dob != None and len(dob.split("-")) != 3:
            return False,"Invalid date"
            
        elif dob != None and (len(dob.split("-")[0]) != 2 or int(dob.split("-")[0]) > 30):
        
            return False,"Invalid date or date out of range"
        
        elif dob != None and (len(dob.split("-")[1]) != 2 or int(dob.split("-")[1]) > 12):
            return False,"Invalid month or month out of range"
        
        elif dob != None and (len(dob.split("-")[2]) != 4 or (datetime.date.today().year - int(dob.split("-")[2]) < 18)):
            return False,"Invalid year or less than 18 years"

        elif (pincode != None and len(pincode) != 3):
            return False,"invalid pincode"
        elif (password != None and len(password) != 4):   # assumption here is user is giving integers
            return False, "Invalid password"
        else:
            return True,None

    def address(self):
        door_no = "123"#input("Door no ")
        street = "test"#input("Street ")
        city = "test" #input("City ")
        pincode = "123"#input("Pincode ")   # 3 digit

        return {"door_no":door_no,"street":street,"city":city,"pin":pincode}

    def authCheck(self):
        account_number = int(input("  Account Number : "))
        docs = self.read()
        print (docs)
        for doc in docs :
            if account_number in doc:
                name = doc[1]
                print (f"Welcome {name} ....")
                password = int(input(" Password ... "))
                if password == doc[4]:
                    return True,doc
                else:
                    return False,"Wrong password"
            else:
                return False,"Account not found"

    def addCustomer(self):
        print ("Custome info here .... ")
        name = "Test"#input("Name ")
        dob = "10-10-1992"#input("Date of birth ")
        account_pin = 9999
        account_number =  CustomerOps.customerNumber
        ssn = input("Enter ssn ")
        addr = self.address()
        validated = self.customer_info_validation(pincode=addr["pin"],ssn=ssn,dob=dob,name=name)
        if (validated[0]):
            self.create(
                        [
                            "name",
                            "dob",
                            "account_number",
                            "account_pin",
                            "ssn",
                            "door_no",
                            "street",
                            "city",
                            "pincode"
                        ],
                        [
                            "'"+name+"'",
                            "'"+dob+"'",
                            account_number,
                            account_pin,
                            "'"+ssn+"'",
                            "'"+addr["door_no"]+"'",
                            "'"+addr["street"]+"'",
                            "'"+addr["city"]+"'",
                            addr["pin"]
                        ])
            
            CustomerOps.customerNumber+=1
        else:
            print (validated)
        return (account_number,name,account_pin)
    def readCustomer(self,conditionData):
        print (self.readById(conditionData))

    def updateCustomer(self):
        pass 

    def deleteCustomer(self):
        pass 
        

# DbOps.host = '127.0.0.1'
# DbOps.port = 3307

# database = 'bank'
# password = 'pMac'
# user = 'root'
# table = 'customers'

# cOps = CustomerOps(database,password,user,table)
# # cOps.addCustomer()
# cOps.readCustomer()


