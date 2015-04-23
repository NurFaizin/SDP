#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from urllib import urlopen
import sys

WORDS_URL = \
    "https://s.sebangsa.net/2015/04/08/197761f727a09d2f3ec4fee86068935b.txt"

WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Buat sebuah class dengan nama %%% yang adalah-sebuah %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% memiliki-sebuah __init__ yang mengambil self dan"
        "parameter *** sebagai parameter input.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% memiliki-sebuah function bernama *** yang mengambil"
        "self dan parameter @@@ sebagai parameter input.",
    "*** = %%%()":
        "Tetapkan *** ke sebuah instance dari class %%%.",
    "***.***(@@@)":
        "Dari *** ambil function ***, dan panggil dengan parameter self, @@@"
        "sebagai parameter input.",
    "***.*** = '***'": "Dari *** ambil atribut *** dan berikan nilai '***'."
}

PHRASE_FIRST = True

# Load up the words from the website
for word in urlopen(WORDS_URL).readlines():
        WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = \
        [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # Fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # Fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # Fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# Keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

                print question

                raw_input("> ")
                print "JAWABANNYA: %s\n\n" % answer
except EOFError:
    print "\nBye"
