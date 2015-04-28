#!/usr/bin/env python
# -*- coding: utf-8 -*-


print "Please enter many 4 digits binary number separated by comma: "
input = raw_input("> ").split(",")	# Get input and split by comma

number = []

for i in input:
    if (int(i, 2) % 5 == 0):	# Convert bin to decimal
        number.append(i)

# Print separated by comma
print (",").join(number)
        
