#!/usr/bin/env python
#! -*- coding:utf-8 -*-

""" a simplest usage of csv.DictReader """

import csv

def csv2dict(csvFile):
	return csv.DictReader(open(csvFile, "rb"))

dic = csv2dict("test.csv")
for d in dic:
	print d
	
