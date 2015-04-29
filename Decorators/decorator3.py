#!/usr/bin/env python
# -*- coding: utf-8 -*-


def logger(func):
    def inner(*args, **kwargs):     # * is list then ** is dictionary
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner

@logger
def foo1(x, y=1):
    return x * y

@logger
def foo2():
    return 2

foo1(5, 4)
foo1(x=5, y=4)
foo1(1)
foo2()
