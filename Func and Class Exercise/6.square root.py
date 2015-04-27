#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

c = 50
h = 30

print "Masukkan deret angka yang dipisahkan dengan tanda koma: "
i = raw_input("> ").split(",")

hasil = []

for d in i:
	akar = math.sqrt((2 * c * int(d))/h)
	akar_rounded = int(round(akar))
	hasil.append(str(akar_rounded))

hasil_joined = (",").join(hasil)
print hasil_joined