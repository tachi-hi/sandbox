#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function Definition
# "#" mark is comment out
def func(): # Do not forget this colon (This seems similar to "{" in C like languages) 
	print u"This is a message (Unicode)" # "u" before the quotation mark indicates "U"nicode 
	print u"Display a Unicode characters 東京都千代田区"

# Strings
def concat_strings(name):
	print u"こんにちは" + name + u"さん"
	# There many functions to process strings.


# Rercursive Function, Ternary Operator (i.e. bool ? val1 : val2 )
def Fib1(n):
	return 1 if n <= 1 else Fib1(n - 1) + Fib1(n - 2)


def Fib2tmp(n, a, b):
	return a if n <= 1 else Fib2tmp(n - 1, a + b, a)

def Fib2(n):
	return Fib2tmp(n, 1, 1)


def Fib3(n, a = 1, b = 1): # default values can be dropped. Fib3(3) means Fib(3,1,1) in this case.
	return a if n <= 1 else Fib2tmp(n - 1, a + b, a)

# if 
def fizzbuzz_test(n):
	if n % 3 == 0 and n % 5 == 0 : #  x % y returns the residual of the division
		print "fizzbuzz"
	elif n % 3 == 0:
		print "fizz"
	elif n % 5 == 0:
		print "buzz"
	else:
		print n
# for
def fizzbuzz(n):
	for i in range(1, n):
		fizzbuzz_test(i)

# Main function
# 
# If this script was called from the shell by the command
# >   python basic_grammar.py
# then probably "__main__" is set to __name__, and following are evaluated, 
# but if __name__ was not "__main__" then the following are not executed.
#
if __name__ == "__main__":
	func()
	concat_strings(u"田中")
	print Fib1(1), Fib1(2), Fib1(3), Fib1(4), Fib1(5), Fib1(6), Fib1(7), Fib1(8), Fib1(9), Fib1(10)
	print Fib2(1), Fib2(2), Fib2(3), Fib2(4), Fib2(5), Fib2(6), Fib2(7), Fib2(8), Fib2(9), Fib2(10), Fib2(100), Fib2(995) # Fib2(1000) failed
	print Fib3(1), Fib3(2), Fib3(3), Fib3(4), Fib3(5), Fib3(6), Fib3(7), Fib3(8), Fib3(9), Fib3(10), Fib3(100), Fib3(995)

	fizzbuzz(20)



