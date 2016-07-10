import shelve
import numpy as np

def f(x):
    return x + 1

# read, write, creatte
db = shelve.open("test.shelve", "c")
db["numpy_object"] = np.asarray([1, 2, 3],dtype=np.float32)
db["fucntion"] = f
# db["lamnba"] = lambda x : x + 1 # this doesn't work
db["dictionary"] = { # complicated object
    "fieldA" : 1,
    "fieldB" : "string",
    "fieldC" : 123456789012345678901234567890,
    "fieldD" : [1,2,3,4,5],
    "fieldE" : 3.141592653589793238462643383279502884197169399375105820974944,
    "fieldF" : {
        "subfieldA": {
            "subsubfieldA": [1,2,3]
        },
        "subfieldB": None
    }
}
db.close()


# read only mode
db_r = shelve.open("test.shelve", "r")
for k, v in db_r.items():
    print(k, v)
db_r.close()
