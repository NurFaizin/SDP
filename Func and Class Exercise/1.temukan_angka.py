#!/usr/bin/env python
# -*- coding: utf-8 -*-

def temukan_angka(awal, akhir):
	angka = []

	for x in range(awal, akhir + 1):
		if (x % 7 == 0 and x % 5 != 0):
				angka.append(str(x))

	print (", ").join(angka)


awal = int(raw_input(
	"Temukan angka yang habis dibagi 7 dan bukan kelipatan 5 mulai dari: "
	))
akhir = int(raw_input("sampai dengan: "))

temukan_angka(awal, akhir)