#!/usr/bin/env python
fahrenheit = 0.0
print "Fahrenheit to Celcius"
while fahrenheit <= 250:
	celcius = (fahrenheit - 32.0) / 1.8
	print "%5.1f %7.2f" % (fahrenheit , celcius)
	fahrenheit = fahrenheit + 25
