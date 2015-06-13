#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals
import json
#import codecs

f = open("designated_cities.json", "r")
#f = codecs.open("designated_cities.json", "r","utf-8")

dat = json.load(f)
f.close()

print json.dumps(dat, ensure_ascii=False, indent = 2)

def printLstUnicode(lst):
	""" UTF-8 のリストは通常では文字化けするが文字化けしないように """
	print "".join("%s, " % i for i in lst) 	


printLstUnicode(dat[i]["pref"] for i in range(0,19))

cityList = [dat[i]["city"] for i in range(0,19)]
printLstUnicode(cityList)



