#!/usr/bin/env python

# alias: cPickle to pickle
# if cPickle does not exist, pickle may be used
try:
   import cPickle as pickle
except:
   import pickle

import numpy



class sampleClass:
    def __init__(self):
        self.num = 12345
        self.str = "This is a string"
        self.array = numpy.arange(10)

    def __eq__(self, rhs):
        return (self.num == rhs.num 
            and self.str == rhs.str 
            and self.array == rhs.array)

    def __str__(self):
        return "* num = " + str(self.num) \
            + "\n* str = " + self.str \
            + "\n* array = " + str(self.array)



def pickle_demo(dat):
    """ serialize the given data and display it """

    print "Original Data: "
    print dat # The serialized data will be displayed.
    print "--------------"

    # pickle
    dat_pkl = pickle.dumps(dat) 
    print "Serialized: "
    print dat_pkl # The serialized data will be displayed.
    print "--------------"

    # unpickle
    dat_unpkl = pickle.loads(dat_pkl)
    print "Deserialized: "
    print dat_unpkl
    print "--------------"

    # test
    print "The same object?: ", (dat is dat_unpkl)
    print "The same content?: ", (dat == dat_unpkl)
    print "------------------------------------------------"    


def test_func():
    cl = sampleClass()
    pickle_demo(cl)

if __name__ == "__main__":
    # demos for simple objects
    pickle_demo(12345)
    pickle_demo(12.345)
    pickle_demo("This is a string")
    pickle_demo(numpy.arange(3))

    #class
    cl = sampleClass()
    pickle_demo(cl)

    test_func()
    
