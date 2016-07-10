# Shelf

see https://docs.python.org/3/library/shelve.html

Similar to dbm/ndbm, but any python object can be inserted.

DB files created by Python 2 and Python 3 may not be compatible.
Python 2 creates single DB file named `test.shelve` while Python 3 produces three files named `test.shelve.bak`, `test.shelve.dat`, and `test.shelve.dir`.
