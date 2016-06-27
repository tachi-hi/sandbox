## about
This is just a memo for me

### Terminology of MongoDB


|Ordinary SQL|MongoDB|Python|
|:---|:---|:---|
|Database|Database||
|Table|Collection|List of Dictionaries|
|Row|Document|Dictionary|
|Column|Field|Key and Value|

They are not exactly the same but similar.

### What to do first

install MongoDB and pymongo. see http://api.mongodb.com/python/current/installation.html

`apt-get install pymongo-python` and `pip install pymongo` may not work successfully.
see also http://stackoverflow.com/questions/13115031/failure-to-import-pymongo-ubuntu/16004833#16004833


Then, activate MongoDB

    mongod

then run the script

    python test.py


### View data via the MongoDB CLI

Run mongo, and show the content of the database as follows.

    mongo

Then

    show dbs
    use test_db
    show collections
    db.test_collection.find() # show all

Try following commands

    db.test_collection.find({'x': 1})                          # find data such that x = 1
    db.test_collection.find({$or :[{'x' : 3}, {'a' : 2}]})     # either x = 3 or a = 2 is satisfied
    db.test_collection.find({x :{$gt: 2}})                     # greater than

If you want to exit, press Ctrl-D.
