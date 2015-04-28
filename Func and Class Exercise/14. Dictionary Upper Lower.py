#!/usr/bin/env python
# -*- coding: utf-8 -*-


dictionary = {'upper':0, 'lower':0}

print "Please input sentence that contain upper and lower char: "
string = raw_input("> ")

# Check all characters
for char in string[0:]:
    if char.isalpha():					# If aplhabet
        if char.isupper():				# If upper case
            dictionary['upper'] += 1
        else:
            dictionary['lower'] += 1

print "UPPER CASE %s" % dictionary['upper']
print "LOWER CASE %s" % dictionary['lower']
