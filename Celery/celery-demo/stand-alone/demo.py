#!/usr/bin/env python
from tasks import penjumlahan


def execAndWait():
    print "set Queue and Wait for Result"
    x = penjumlahan.delay(2, 4)

    while True:
        if x.ready():
            print "result found!"
            print x.get()
            break

        else:
            print "belum dapat result..."


def inCeleryWeTrust():
    print "In Celery We Trust. Queue and Forget"
    penjumlahan.delay(2, 4)


if __name__ == '__main__':
    inCeleryWeTrust()
