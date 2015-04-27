#!/usr/bin/env python
# -*- coding: utf-8 -*-

def faktorial(n):
	if (n == 0):
		return 1
	else:
		return n * faktorial(n - 1)

n = int(raw_input("Nilai faktorial dari: "))
print faktorial(n)