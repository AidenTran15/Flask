import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initailize():
        client = pymongo.MongoClient(Database.URI)
        Database.Database = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, data):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, data):
        return Database.DATABASE[collection].find_one(query)
        
