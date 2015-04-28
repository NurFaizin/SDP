#!/usr/bin/env python
# -*- coding: utf-8 -*-


log = []
saldo = 0

print """Please input the transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
-----------------------------------------"""

while True:
	line = raw_input()
	
	if not line:
		break

	log.append(line)

for t in log:
    trans = t.split()
    
    if (trans[0] == "D"):
        saldo += int(trans[1])
    elif (trans[0] == "W"):
        saldo -= int(trans[1])
        
print saldo
