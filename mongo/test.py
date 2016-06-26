
from pymongo import MongoClient

def insert_example(db_connect):
    """ insert data to the collection """
    db_connect["test_collection"].insert_one({'x':1})
    db_connect["test_collection"].insert_one({'x':1, 'a':2})

    db_connect["test_collection"].insert_one({'x':2})
    db_connect["test_collection"].insert_one({'x':3})
    db_connect["test_collection"].insert_one({'x':4})

    # many data with different _id
    db_connect["test_collection"].insert_one({'x':5})
    db_connect["test_collection"].insert_one({'x':5})
    db_connect["test_collection"].insert_one({'x':5})
    db_connect["test_collection"].insert_one({'x':5})
    db_connect["test_collection"].insert_one({'x':5})
    db_connect["test_collection"].insert_one({'x':5})

    # insert many data simultaneously
    db_connect["test_collection"].insert_many([
        {'y':i, 'z': 20 - i} for i in range(20)]
    )
    db_connect["test_collection"].insert_many([
        {"y":8, "z": 100 + i} for i in range(5)]
    )

def show_example(db_connect):
    """ show all data """
    lst = db_connect["test_collection"].find()
    print("* all data")
    if not lst.count() == 0:
        for x in lst:
            print(x)
    else:
        print("empty")
    print("================================")

def show_example_2(db_connect):
    query = {"$and":
        [{"y":{"$gt": 7}},
         {"z":{"$gt": 8}}
        ]
    }
    lst = db_connect["test_collection"].find(query)

    print("* data s.t. y > 7 and z > 8")
    if not lst.count() == 0:
        for x in lst:
            print(x)
    else:
        print("empty")
    print("================================")

def remove_example(db_connect):
    print("remove a data that contain \"y = 8\" is deleted.")
    db_connect["test_collection"].delete_one({'y': 8})
    show_example_2(db_connect) # no data is deleted

    print("remove a data that contain \"y = 8\" is deleted. (2nd time)")
    db_connect["test_collection"].delete_one({'y': 8})
    show_example_2(db_connect) # no data is deleted

    print("remove a data that contain \"y = 8\" is deleted. (3rd time)")
    db_connect["test_collection"].delete_one({'y': 8})
    show_example_2(db_connect) # no data is deleted

    print("remove ALL data that contain \"y = 8\" are deleted.")
    db_connect["test_collection"].delete_many({'y': 8})
    show_example_2(db_connect) # no data is deleted

    print("remove all data")
    db_connect["test_collection"].delete_many( {} ) # empty dictionary
    show_example_2(db_connect) # no data is deleted

    show_example(db_connect)


if __name__ == "__main__":

    mongo_client = MongoClient('localhost:27017')
    db_connect = mongo_client["test_db"] # create test_db

    insert_example(db_connect)

    show_example(db_connect)
    show_example_2(db_connect)

    remove_example(db_connect)
