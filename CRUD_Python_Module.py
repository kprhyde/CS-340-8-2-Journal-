# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS, HOST, PORT, DB, COL): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'enter' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Method to implement the C in CRUD. 
    def create(self, data): # Key/Value creation
        if data is not None: # Creates new object if acceptible input
            self.database.animals.insert_one(data)  # data should be dictionary
            return True 
        else: # Creation was unsuccessful, outputs message, and returns false
            return False

    # Method to implement the R in CRUD.
    def read(self, query): # Key/Value lookup 
        if query is not None: # Query exists, returns every object associated with "query"
            cursor = self.database.animals.find(query)
            result = list(cursor) # Creates a list of the object.
            return result
        else: # Query doesn't exist outputting an empty list
            return [] 
    
    # Methods to implement the U in CRUD. 
    def update(self, query, updates): # Key/Value lookup
        modNum = 0 
        if query is not None: # Checks to ensure query exists then updates with the new updates.
            result = self.database.animals.update_one(query, updates)
            if result.modified_count > 0:
                modNum = result.modified_count
                return print(modNum) # Returns number of one object that have been modified.
            else:
                return print(modNum)
        else:
            return print(modNum)
    
    def updateMany(self, query, updates):
        modNum = 0
        if query is not None: # Checks to ensure query exists then updates with the new updates.
            result = self.database.animals.update_many(query, updates)
            if result.modified_count > 0:
                modNum = result.modified_count
                return print(modNum) # Returns number of all objects that have been modified.
            else:
                return print(modNum)
        else:
            return print(modNum)
        
    # Method to implement the D in CRUD.
    def delete(self, data):
        delNum = 0
        if data is not None: # Checks to ensure data exists then deletes the first one.
            result = self.database.animals.delete_one(data)
            if result.deleted_count > 0:
                delNum = result.deleted_count
                return print(delNum) # Returns number of one object that has been deleted.
            else:
                return print(delNum)
        else:
            return print(delNum)