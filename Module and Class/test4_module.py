#!/usr/bin/env python
# -*- coding: utf-8 -*-


# This is class
class Car(object):

    # This is function
    def car_price(self, tahun, warna):
        if (tahun < 2000 and warna == "hitam"):
            print "Harga mobil tahun %d warna %s adalah 1 juta" % (
                tahun, warna
            )
        elif (tahun >= 2000 and warna == "merah"):
            print "Harga mobil tahun %d warna %s adalah 2 juta" % (
                tahun, warna
            )
        else:
            print "Harga mobil tahun %d warna %s tidak diketahui" % (
                tahun, warna
            )
