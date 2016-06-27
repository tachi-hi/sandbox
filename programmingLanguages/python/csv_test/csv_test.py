#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import csv

def delEmpty(line):
	return [i for i in line if i != '']
	
def csvparse(csvFile):
	dat = csv.reader(open(csvFile,"rb"))
	for row in dat:
		if row != []:
			print delEmpty(row)
		else:
			pass



csvparse("test.csv")
