#!/usr/bin/env python
for x in range(1, 100):
	prima = True
	for y in range(2, 10):
		if x != y and x % y == 0 or x == 1:
			prima = False
			break
	if prima:
		print x
