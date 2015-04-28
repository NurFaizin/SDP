#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import Counter

# Get input and split it
print "Please input the sentence: "
words = raw_input("> ").split()		# Get input and split by comma

# Counter frequency of word
words_count = Counter(words)

# Print with sorted by key
for key in sorted(words_count):
    print "%s: %s" % (key, words_count[key])
