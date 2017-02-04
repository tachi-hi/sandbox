#!/usr/bin/env python 
# -*- coding: utf-8 -*-

" os: open stream? output stream? operating system? (probably the last one) "
import os 

print os.getenv("PATH") # get $PATH

print os.getcwd()  # current workind directory

print os.getpid()  # get process id
print os.getppid() # get parent process id


"""
 Write something to a file
 open tmp.txt (write only) This is different from os.open()
"""
f = open("tmp.txt","w")
f.write("aaa\n")
print "%d%s" % (1, "test")  # similar to printf("%d%s",1,"test"); in C. 
                             # The arguments should be packed in a tuple? 
                             # (It did not work when it was a list)
f.write("%d\n" % 1) 
f.write("%f %f" % (
			1,
			(lambda x,y: x + y)(1,2)
			))
f.close()


g = open("tmp.txt","r")
print g.read() # It may depend on the environment but g.read() before f.close() did not work in my environment
g.close()



"""
 Template and substitution
 It seems more sophisticated than the style "%d%d%d" % (1,2,3)
"""
from string import Template

myTemplate = Template("My name is ${name}. I am from ${prefecture}.")
s1 = myTemplate . substitute ( name = "Hanako", prefecture = "Tokyo")
s2 = myTemplate . substitute ( name = "Taro", prefecture = "Hokkaido")
print s1
print s2



