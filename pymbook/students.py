#!/usr/bin/env python
n = int(raw_input("Enter the number of students: "))
data = {}
languages = ('Physics', 'Maths', 'History')
for i in range(0, n):
	name = raw_input('Enter the name of students %d: ' % (i + 1))
	marks = []
	for x in languages:
		marks.append(int(raw_input('Enter marks of %s: ' % x)))
	data[name] = marks
for x, y in data.iteritems():
	total = sum(y)
	print "%s's total marks %d" % (x, total)
	if total < 120:
		print "%s failed :(" % x
	else:
		print "%s passed :)" % x
