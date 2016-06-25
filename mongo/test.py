
from pymongo import MongoClient

if __name__ == "__main__":

    mongo_client = MongoClient('localhost:27017')
    db_connect = mongo_client["test_db"] # create test_db

    # insert data to the collection
    db_connect["test_collection"].insert_one({'x':1})
    db_connect["test_collection"].insert_one({'x':1, 'a':2})
    db_connect["test_collection"].insert_one({'x':2})
    db_connect["test_collection"].insert_one({'x':3})
    db_connect["test_collection"].insert_one({'x':4})
    db_connect["test_collection"].insert_one({'x':5})
