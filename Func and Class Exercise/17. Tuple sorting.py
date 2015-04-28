#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


from operator import itemgetter, attrgetter

print "Please input multi name,age,score: "

buff = []
tuples = []

# Get input multiline
while True:
	line = raw_input()
    
	if not line:
		break

	buff.append(line)

# Convert to tuple
for x in buff:
    y = x.split(",")
    tuples.append(tuple(y))

# Sorted tuple by multiple element
tuples_sorted = sorted(
        tuples, key=lambda element: (element[0], element[1], element[2])
    )

# Print tuple    
print tuples_sorted
