#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Masukkan deret angka yang dipisahkan dengan tanda koma: "
deret = raw_input("> ").split(",")

print "#list"
print deret

print "#tuple"
print tuple(deret)