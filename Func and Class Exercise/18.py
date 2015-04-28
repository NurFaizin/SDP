#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Initiate generator
def createGenerator(n):
    mylist = range(1, n)
    for i in mylist:
       if (i % 7 == 0):
           yield i

mygenerator = createGenerator(20)

for i in mygenerator:
    print i
