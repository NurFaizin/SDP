#!/usr/bin/env python
# -*- coding: utf-8 -*-


print "Please enter many 4 digits binary number separated by comma: "
input = raw_input("> ").split(",")
number = []

for i in input:
    if (int(i, 2) % 5 == 0):
        number.append(i)

print ", ".join(number)
        
