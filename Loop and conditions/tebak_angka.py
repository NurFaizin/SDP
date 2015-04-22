#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

print "Halo! Siapa nama Anda?"
nama = raw_input("> ")

print "Hallo %s, saya sedang membayangkan satu angka antara 1 " \
    "sampai dengan 20." % nama

angka = randint(1, 20)  # Get random int
lagi = True
hitung = 1  # Counter

while(lagi):
    print "Tebak angka yang dimaksud."
    tebakan = int(raw_input("> "))

    if(tebakan == angka):
        print "Selamat, %s! Anda menebak angka saya di %d tebakan!" % (
            nama, hitung
        )
        lagi = False
    elif(tebakan <= angka):
        print "Tebakan angka Anda terlalu rendah."
        hitung = hitung + 1
    elif(tebakan >= angka):
        print "Tebakan angka Anda terlalu tinggi."
        hitung = hitung + 1
