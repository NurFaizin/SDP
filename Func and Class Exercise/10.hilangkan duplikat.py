#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Masukkan sebuah kalimat: "

kalimat = raw_input("> ").split()

kalimat_unik = list(set(kalimat))

print " ".join(sorted(kalimat_unik))
