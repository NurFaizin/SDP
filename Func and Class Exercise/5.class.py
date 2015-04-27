#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StringClass(object):
	"""docstring for StringClass"""
	def __init__(self, param):		
		self.getString(param)


	def getString(self, string):
		self.string = string


	def printString(self):
		print self.string.upper()



string = StringClass("asda")
string.printString()
