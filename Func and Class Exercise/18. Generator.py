#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Generator definition
def createGenerator(n):
    mylist = range(1, n)
    for i in mylist:
       if (i % 7 == 0):
           yield i 	# Like return

# Initiate generator
mygenerator = createGenerator(20)

# Iterate generator
for i in mygenerator:
    print i
