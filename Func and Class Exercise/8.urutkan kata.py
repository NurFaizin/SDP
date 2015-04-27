#!/usr/bin/env python
# -*- coding: utf-8 -*-


print "Masukkan deret kata yang dipisahkan dengan tanda koma: "
words = raw_input("> ").split(",")

words_sorted = sorted(words)

print (",").join(words_sorted)