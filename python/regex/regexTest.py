#!/usr/bin/env python
# -*- coding:utf-8 -*-

# This code snippet converts 'pred(x)' to 'R("pred", x)'
#
# predicate list: isDigit, isChar, isString
#
# usage (example):
#   echo "isDigit(3) isChar(\"a\") isString(\"a_b_c\")" | python regexTest.py

import re # regex
import sys # stdin

for line in sys.stdin:
	p = re.compile('(isDigit|isChar|isString)\(([a-zA-z0-9_\"]+)\)')
	out = p.sub(r'R("\1", \2)', line) # (something) -> \number
	print out, # prohibit "print" to print "\n"
