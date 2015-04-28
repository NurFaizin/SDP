#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define class
class StringClass(object):
	"""docstring for StringClass"""
	def __init__(self, param):		
		self.getString(param)	# Call some methods while initiation

	# Method to get string and save to attribute
	def getString(self, string):
		self.string = string

	# Method to print some attributes
	def printString(self):
		print self.string.upper()


# Class initiation
string = StringClass("Hello Class!")

# Call some methods
string.printString()
