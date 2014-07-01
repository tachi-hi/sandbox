#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------
#List Conprehension :basic
#-------------------------------------------------------------------------------------------------
a = [x for x in range(10) if x % 3 == 0]
print a


# More Complicated One
def fizzbuzz (x):
	return "fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else x
	
b = [fizzbuzz(x) for x in range(1,100)]
print b

# Using Lambda 

c = [(lambda x: "fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else x)(x) for x in range(1,100)]
print c


# This may be more readable
# Indents and whitespaces inside of the List do not have any syntactic function?
d = [(lambda a:
		     "fizzbuzz"	if a % 15 == 0 
		else "fizz"		if a % 3 == 0 
		else "buzz"		if a % 5 == 0 
		else a) (x)
	for x in range(1,100)]
print d


#-------------------------------------------------------------------------------------------------
# Operations on List
#-------------------------------------------------------------------------------------------------

print d.count("fizz") # count how many times "fizz" appeard in the List.

e = d.remove("fizz") # ".remove" does not return the result. ".remove" operates the object itself.
print d
print e

c.sort() # This is similar to "remove". The result overwrites the original data.
print c


#-------------------------------------------------------------------------------------------------
# filter, map, reduce
#-------------------------------------------------------------------------------------------------

print filter( # extract what matches the function from the list
		(lambda x: x % 2 == 0), # function that returns bool
		[x for x in range(10)]) # list

print map( # apply the function to the each element of the list
		(lambda x: x * 3), # function
		[x for x in range(10)]) # list

print reduce( # fold the list with the function below
		(lambda x, y:  x + y), # function. Note (lambda (x,y): x + y) is invalid. It means the argument of the function is a tuple with two elements.
		[x for x in range(10)]) # list




