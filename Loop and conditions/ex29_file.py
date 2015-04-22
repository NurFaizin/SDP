#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "You enter a dark room with two doors. Do you go through door #1" \
    "or door #2?"

pintu = raw_input("> ")

if pintu == "1":
    txt = open("pintu1.txt")
    choices = txt.read().splitlines()  # splitlines will get lines without \n

    print "There's a giant bear here eating a cheese cake. What do you do?"

    idx = 0
    print "{0}. {1}".format(idx + 1, choices[idx])

    idx = idx + 1
    print "{0}. {1}".format(idx + 1, choices[idx])

    beruang = raw_input("> ")

    if beruang == "1":
        print "The bear eats your face off. Good job!"
    elif beruang == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well doing {0} is probably better. Bear runs away.".format(
            beruang
        )
elif pintu == "2":
    txt = open("pintu2.txt")
    choices = txt.read().splitlines()  # splitlines will get lines without \n

    print "You stare into the endless abyss at Cthulhu's retina."

    idx = 0
    print "{0}. {1}".format(idx + 1, choices[idx])

    idx = idx + 1
    print "{0}. {1}".format(idx + 1, choices[idx])

    idx = idx + 1
    print "{0}. {1}".format(idx + 1, choices[idx])

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good Jod!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
