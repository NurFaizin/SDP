#!/usr/bin/env python
# -*- coding: utf-8 -*-

i = raw_input("Masukkan angka: ")
d = dict()

for x in range(1,int(i) + 1):
	d[x] = x * x

print d