#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Get multiline input
buff = []
while True:
	line = raw_input()
	
	if not line:
		break

	buff.append(line)

# Print with upper case
for line in buff:
	print line.upper()
