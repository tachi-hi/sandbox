
from pymongo import MongoClient
from datetime import datetime

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

    # specials
    db_connect["test_collection"].insert_one({'日本語':5})
    db_connect["test_collection"].insert_one({'time':datetime(2016,7,2,2,31,0)})
    db_connect["test_collection"].insert_one({'time':datetime(2015,7,2,2,31,0)})
    db_connect["test_collection"].insert_one({'time':datetime(2015,1,1,0,1,0)})
    db_connect["test_collection"].insert_one({'time':datetime(2015,1,1,0,0,0)})
    db_connect["test_collection"].insert_one({'time':datetime(2014,7,2,2,31,0)})
    db_connect["test_collection"].insert_one({'time':datetime(2013,7,2)})
    db_connect["test_collection"].insert_one({'time':datetime(1995,7,2)})
    db_connect["test_collection"].insert_one({'time':datetime(3,7,2)})

    # What if there exist duplicate keys in a single document:
    db_connect["test_collection"].insert_one({'x':100, 'x': -100})
    # This is actually valid, but the result is {'x' : -100}.

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
         {"z":{"$gt": 8}} # $gt, $gte, $lt, $lte, $ne
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

def show_example_3(db_connect):
    query = {"time" : {"$gt" : datetime(2015,1,1)}}
    lst = db_connect["test_collection"].find(query)
    print("date after (>) ", datetime(2015,1,1))
    for l in lst:
        print(l)

    query = {"time" : {"$gte" : datetime(2015,1,1)}}
    lst = db_connect["test_collection"].find(query)
    print("date after (>=) ", datetime(2015,1,1))
    for l in lst:
        print(l)

    query = {"time" : {"$lt" : datetime(2003,1,1)}}
    lst = db_connect["test_collection"].find(query)
    print("date before ", datetime(2003,1,1))
    for l in lst:
        print(l)

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

def update_example(db_connect):
    """ insert new field to an existing data """
    db_connect["test_collection"].update({'y': 8}, {'hoge': 1000})
    # This replaces a document s.t. y = 8 by {'hogehoge': 1000}.

    db_connect["test_collection"].update({'y': 8}, {"$set": {'piyo': 1000}})
    # This adds a field {'hogehoge': 1000} to a document s.t. y = 8

    db_connect["test_collection"].update({'y': 8}, {"$set": {'z': 'we are updated'}}, multi=True)
    # apply the rule to all the document that satisfy the condition

    print("$set can be used when we create a new field, as well as when we update the value of a field")
    print("This \"$set\" is verb. Not noun. Not \"set theory\"")
    show_example(db_connect)



if __name__ == "__main__":

    mongo_client = MongoClient('localhost:27017')
    db_connect = mongo_client["test_db"] # create test_db

    insert_example(db_connect)

    show_example(db_connect)
    show_example_2(db_connect)

    remove_example(db_connect)

    insert_example(db_connect)
    update_example(db_connect)

    show_example_3(db_connect)
