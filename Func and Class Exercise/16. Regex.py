#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
regex_criteria = "^(?=.*[a-z])(?=.*\d)(?=.*[A-Z])(?=.*[$#@]).{6,12}$"

print "Import multi password separated by comma:"
passwords = raw_input("> ").split(",")		# Get input and split by comma

for password in passwords:
    if (re.search(regex_criteria, password)):
        print password
