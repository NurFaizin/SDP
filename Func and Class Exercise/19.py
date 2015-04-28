#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import Counter

print "Please input the sentence: "
words = raw_input("> ").split()

words_count = Counter(words)

for key in sorted(words_count):
    print "%s: %s" % (key, words_count[key])
