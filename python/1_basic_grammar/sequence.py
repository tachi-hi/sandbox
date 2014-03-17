#!/usr/bin/env python
# -*- codint: utf-8 -*-

" Python has some `sequences' " # Strings also can be used as "comment out" 

" List " 

a = [1, 2, 3, 4, 5, "string", (6, 7)] # Types of all the elements need not be identical

" Tuple "

b = (1, 2, 3, 4, 5, "string", [6, 7])

" String "

c = "String"

# Each 

if __name__ == "__main__":
	print a[0], b[0], c[0] # Index starts by 0
	print a[0:3], b[0:3], c[0:3]# range
	print a[1:3], b[1:3], c[1:3]# range

	print "a[start:end]	 is basically a[start] to a[end-1]"
		
	print a[-1], c[-1] # -1 returns the last element 

	print len(a) #returns length

	for i in range(0,8): # for(i = 0; i < 8; i++)
		print i
		print a[0:i]
		print b[0:i]
		
	print "Arithmetic Operation: Addition is concatenation"
	print [1,2,3] + [1,2,3] #[1,2,3,1,2,3]
	print (1,2,3) + (1,2,3) #(1,2,3,1,2,3)

	print "Arithmetic Operation: Multiplication is also concatenation"
	print [1,2,3] * 3 #[1,2,3,1,2,3,1,2,3] 
	print (1,2,3) * 3 #(1,2,3,1,2,3,1,2,3)
	
	
