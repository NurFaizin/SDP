#!/usr/bin/env python
# -*- coding: utf-8 -*-

even_number = []

for i in range(2000, 3000 + 1):
    if (i % 2 == 0):
        even_number.append(str(i))

print ",".join(even_number)
    
