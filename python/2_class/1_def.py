#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition of Class
class Animal:
	def __init__(self, arg1, arg2): # This is similar to "constructor" of C++
		self.age = arg1
		self.sex = arg2

	# Member functions (methods) are defined as 
	def print_age(self):
		print self.age

	def print_sex(self):
		print self.sex

	def __str__(self): # There are many functions of this kind.
		return "This is animal"

#Subclass
class Dog(Animal): 
	def __init__(self, arg1, arg2, arg3):
		Animal.__init__(self, arg2, arg3) # call the "constructor" of the superclass
		self.name = arg1

	def print_name(self):
		print self.name

class Horse(Animal):
	def __init__(self, arg1, arg2, arg3):
		Animal.__init__(self, arg2, arg3)
		self.ownername = arg1

	def print_ownername(self):
		print self.ownername
		
# (*)
dog2 = Dog(u"ショコラ", 3, "メス")


# main
if __name__ == "__main__":
	dog = Dog(u"ポチ", 3, "オス")
	dog.print_name()
	dog.print_age()
	dog.print_sex()

	horse = Horse(u"田中太郎", 4, "メス")
	horse.print_ownername()
	horse.print_age()
	horse.print_sex()

	# These classes can be instantiated outside of the "main". They may be placed at (*) above. Indeed,
	dog2.print_name()
	dog2.print_age()
	dog2.print_sex()

	print horse # Animal.__str__() is called

	
