#!/usr/bin/env python
# -*- coding: utf-8 -*-


buff = []
while True:
	line = raw_input()
	
	if not line:
		break

	buff.append(line)

for line in buff:
	print line.upper()
