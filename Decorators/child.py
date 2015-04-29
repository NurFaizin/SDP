#!/usr/bin/env python
# -*- coding: utf-8 -*-


from composition import Other

class Child(object):
    def __init__(self):
        self.other = Other()

    def ovveride(self):
        print "Child ovveride()"

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print "Child, before Other altered()"
        self.other.altered()
        print "Child, after Other altered()"

son = Child()
son.ovveride()
son.implicit()
son.altered()
