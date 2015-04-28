#!/usr/bin/env python
# -*- coding: utf-8 -*-


dictionary = {'letter':0, 'digit':0}

print "Please input sentence that contain number and alpha words: "
string = raw_input("> ")

for char in string[0:]:
    if char.isdigit():
        dictionary['digit'] = dictionary['digit'] + 1
    elif char.isalpha():
        dictionary['letter'] = dictionary['letter'] + 1

print "LETTERS %s" % dictionary['letter']
print "DIGITS %s" % dictionary['digit']
