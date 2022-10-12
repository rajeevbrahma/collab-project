import mysql.connector

class DbOps:

    host = None     # class variable
    port = None     # class variable
    
    def __init__(self,database,password,user,table):
        self.database = database 
        self.user = user                    # normal
        self.__password = password          # private
        self.table = table
        self.connect()
    def connect(self):
        self.dbConnection = mysql.connector.connect(
                                            host=self.host,
                                            user=self.user,
                                            password=self.__password,
                                            database=self.database,
                                            port=self.port,
                                            autocommit=True
                                        )
        # prepare a cursor object using cursor() method
        self.cursor = self.dbConnection.cursor() 
        
    def fetchDbVersion(self):
        self.cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        version = self.cursor.fetchone()
        print ("Database version : %s " % version)

    def disConnect(self):
        self.dbConnection.close() 

    def __prepareInsertQuery(self,columns,values):
        queryColumns = ""
        for col in columns:
            queryColumns+=col+","
        queryColumns = queryColumns[:-1]

        queryValues = ""
        for val in values:
            queryValues+=str(val)+","
        queryValues = queryValues[:-1]

        return queryColumns,queryValues

    def __prepareUpdateQuery(self,data):
        update_columns_values = ""
        for col,val in data:
            update_columns_values+=col+"="+str(val)+","
        update_columns_values = update_columns_values[:-1]

        return update_columns_values        

    def create(self,columns,values):
        queryColumns,queryValues = self.__prepareInsertQuery(columns,values)
        query = f"INSERT INTO {self.table} ({queryColumns}) VALUES ({queryValues});"
        print (query)
        self.cursor.execute(query)
        
    def read(self):
        self.cursor.execute(f"SELECT * FROM {self.table};")
        result = self.cursor.fetchall() 
        docs = []
        for doc in result:
            print (doc)
            docs.append(doc)
        return docs

    def readById(self,data):
        condition = data["condition"]
        value = data["value"]
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE {condition}={value};") 
        result = self.cursor.fetchone()
        print (result)

    def update(self,conditionData,data):
        condition = conditionData["condition"]
        value = conditionData["value"]
        update_columns_values = self.__prepareUpdateQuery(data)
        print (update_columns_values)
        self.cursor.execute(f"UPDATE {self.table} SET {update_columns_values} WHERE {condition}={value};") 
        return True
        
    def delete (self,data):
        condition = data["condition"]
        value = data["value"]
        self.cursor.execute(f"DELETE FROM {self.table} WHERE {condition}={value};") 
