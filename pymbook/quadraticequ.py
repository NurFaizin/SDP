#!/usr/bin/env python
import math
a = int(raw_input("a: "))
b = int(raw_input("b: "))
c = int(raw_input("c: "))
d = b * b - 4 * a * c
if d < 0:
	print "ROOTS are imaginary"
else:
	root1 = (-b + math.sqrt(d)) / (2.0 * a)
	root2 = (-b - math.sqrt(d)) / (2.0 * a)
	print "Root 1 = ", root1
	print "Root 2 = ", root2
