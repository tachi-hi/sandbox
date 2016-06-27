#!/usr/bin/env python
#! -*- coding: utf-8 -*-


template = "This is a template. {a} {b}"
template = template.format(a="test1",b="test2")
print template


# dictionary
mes = "My name is {name}. I am from {nationality}. I am {age} years old."
dic=[
	{"name":"Taro", "nationality":"Japan", "age":21},
	{"name":"John", "nationality":"US", "age":22}]

for d in dic:
	print mes.format(**d)
