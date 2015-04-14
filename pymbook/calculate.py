#!/usr/bin/env python
amount = float(raw_input("Enter amount: "))
inrate = float(raw_input("Enter interest rate: "))
period = float(raw_input("Enter period: "))
value = 0
year = 1
while year <= period:
	value = amount + (inrate * amount)
	print "Year %d Rp. %.2f" % (year, value)
	amount = value
	year = year + 1
