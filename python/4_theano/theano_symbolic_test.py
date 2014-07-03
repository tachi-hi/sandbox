#!/usr/bin/env python
# *-* coding: utf-8 -*-

import numpy
import theano
import theano.tensor as T
from theano import function
from theano import pp # pretty-print

"""
Memo for me:

1. First, install theano using python-pip
>> sudo apt-get install python-pip
>> sudo pip install Theano



"""

# matrix
A = T.dmatrix("A") # dmatrix is a matrix of "double" numbers
B = T.lmatrix("B") # lmatrix is a matrix of "long int" numbers
print pp(A)
print pp(B)


# vector
x = T.dvector("x")
print pp(x)


# scalar
d = T.dscalar("d")
print pp(d)

# Basic arithmetic operations are simply written as follows
e = d**2 # d^2
C = A*2  # A * 2
D = A * A # This may be the element-wise multiplication
print pp(e)
print pp(C)
print pp(D)

#------------------------------------------------------------------------------
def test():
	x = T.dscalar("x")
	f = function([x], T.exp(-x ** 2)) # function f(x) = e^(-x^2)
	y = T.exp(-x**2)
	g = function([x], x ** 2 + 2 * x) # function g(x) = x^2 + 2x
	print f(0), g(1)
	print pp(y)                      # pp shows the definitionsof the argument by a user-friendly style
	return

#------------------------------------------------------------------------------
def givens_test():                               # givens: substitute a variable by an expression
	(x, y) = T.dscalars("x", "y")                # Define multiple variables simultaneously
	f = function([x], y**2, givens = [(y, 1/x)]) # f(x) = y^2, where y = 1/x
	print f(2)
	return 

#------------------------------------------------------------------------------
def theano_define_function():
	(x, y, z) = T.dscalars("x", "y", "z")

	# (1)
	z = x * y                   # Bind z to x * y
	f = function([x,y], z)      # This converts z = x * y into a function
	print pp(z)                # f below (2) cannot be displayed by pp. This may be the advantage of this style (1)
	# print pp(f)               # !! This fails

	# (2)
	f = function([x,y], x*y) 	# This seems simpler than the definition above (1)
	print f(1,2)
	return

#------------------------------------------------------------------------------
def matrix_prod():
	A = T.dmatrix("A")
	X = T.dmatrix("X")
	x = T.dvector("x")

	B = T.dot(A, x)   # Dot product, B = A x?
	print pp(B)

	C = T.outer(x, x) # Outer product
	C = T.dot(A,X)
	print pp(C)

	D = T.sqrt(A) # Is this element wise? or D^2 = A?
	print pp(D)

	y = T.dscalar("y")
	E = T.sqrt(y) * T.sqrt(y)
	print pp(E)      # sqrt(y) * sqrt(y) may not be reduced to y automatically
	return 
	
#------------------------------------------------------------------------------
if __name__ == "__main__":
	test()
	givens_test()
	theano_define_function()
	matrix_prod()
	

