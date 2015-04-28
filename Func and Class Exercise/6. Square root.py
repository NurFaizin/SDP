#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

c = 50
h = 30

print "Masukkan deret angka yang dipisahkan dengan tanda koma: "
i = raw_input("> ").split(",")	# Get input and split by comma

hasil = []

for d in i:
	akar = math.sqrt((2 * c * int(d))/h)	# Get formula result
	akar_rounded = int(round(akar))			# Get round number
	hasil.append(str(akar_rounded))

# Print separated by comma
hasil_joined = (",").join(hasil)
print hasil_joined