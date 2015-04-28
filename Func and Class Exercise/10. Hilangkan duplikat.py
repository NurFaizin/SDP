#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Masukkan sebuah kalimat: "

kalimat = raw_input("> ").split()

# Remove duplicate elements
kalimat_unik = list(set(kalimat))

# Print separated by space
print (" ").join(sorted(kalimat_unik))
