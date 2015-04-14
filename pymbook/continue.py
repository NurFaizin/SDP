#!/usr/bin/env python
while True:
	n = int(raw_input("Please enter an Integer: "))
	if n < 0:
		continue
	elif n == 0:
		break
	print "Square is ", n ** 2
print "Bye"
