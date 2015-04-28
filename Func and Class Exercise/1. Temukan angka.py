#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Define function
def temukan_angka(awal, akhir):
	angka = []

	# Get numbers that divisible by 7 but not 5
	for x in range(awal, akhir + 1):
		if (x % 7 == 0 and x % 5 != 0):
				angka.append(str(x))

	# Print separated by comma
	print (",").join(angka)


# Get input
awal = int(raw_input(
	"Temukan angka yang habis dibagi 7 dan bukan kelipatan 5 mulai dari: "
	))
akhir = int(raw_input("sampai dengan: "))

# Call function
temukan_angka(awal, akhir)