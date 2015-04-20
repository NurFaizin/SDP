#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pecah_kata(stuff):
    """Fungsi ini akan memecah kata."""
    words = stuff.split(' ')
    return words


def urutkan_kata(words):
    """Urutkan kata."""
    return sorted(words)


def cetak_kata_pertama(words):
    """Cetak kata pertama."""
    word = words.pop(0)
    print word


def cetak_kata_terakhir(words):
    """Cetak kata terakhir."""
    word = words.pop(-1)
    print word


def urutkan_kalimat(sentence):
    """Takes in a full sentences and return the sorted words."""
    words = pecah_kata(sentence)
    return urutkan_kata(words)


def cetak_pertama_dan_terakhir(sentence):
    """"Cetak kata pertama dan terakhir dari kalimat"""
    words = pecah_kata(sentence)
    cetak_kata_pertama(words)
    cetak_kata_terakhir(words)


def cetak_pertama_dan_terakhir_terurut(sentence):
    """Urutkan kata kemudian cetak yang pertama dan terakhir."""
    words = urutkan_kalimat(sentence)
    cetak_kata_pertama(words)
    cetak_kata_terakhir(words)

print "Let's practice everything."
print """You\'d need to know \'bout escapes with \\ that 
    do \n newlines and \t tabs"""

puisi = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
