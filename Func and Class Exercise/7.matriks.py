#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Masukkan dimensi matriks dipisahkan dengan tanda koma: "
dimensi = raw_input("> ").split(",")

kolom = int(dimensi[1])
baris = int(dimensi[0])

hasil = []

for x in range(0, baris):
	z = []
	for y in range(0, kolom):
		z.append(x*y)

	hasil.append(z)

print hasil  