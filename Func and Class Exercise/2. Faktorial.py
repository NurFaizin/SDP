#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Recursive function
def faktorial(n):
	if (n == 0):
		return 1
	else:
		return n * faktorial(n - 1)		# Call self function

n = int(raw_input("Nilai faktorial dari: "))
print faktorial(n)