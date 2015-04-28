#!/usr/bin/env python
# -*- coding: utf-8 -*-


log = []
saldo = 0

print """Please input the transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
-----------------------------------------"""

# Get input multiline
while True:
	line = raw_input()
	
	if not line:
		break

	log.append(line)

# Count the balance
for t in log:
    trans = t.split()
    
    if (trans[0] == "D"):		# D for Debit
        saldo += int(trans[1])
    elif (trans[0] == "W"):		# W for withdraw
        saldo -= int(trans[1])

# Print balance        
print saldo
