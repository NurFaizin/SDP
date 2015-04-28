#!/usr/bin/env python
# -*- coding: utf-8 -*-


dictionary = {'upper':0, 'lower':0}

print "Please input sentence that contain upper and lower char: "
string = raw_input("> ")

for char in string[0:]:
    if char.isalpha():
        if char.isupper():
            dictionary['upper'] += 1
        else:
            dictionary['lower'] += 1

print "UPPER CASE %s" % dictionary['upper']
print "LOWER CASE %s" % dictionary['lower']
