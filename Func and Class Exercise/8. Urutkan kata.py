#!/usr/bin/env python
# -*- coding: utf-8 -*-


print "Masukkan deret kata yang dipisahkan dengan tanda koma: "
words = raw_input("> ").split(",")

# Sorted list
words_sorted = sorted(words)

# Print separated by comma
print (",").join(words_sorted)