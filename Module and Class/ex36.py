#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Create a mapping of state to abbreviation
bagian = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
kota = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
kota['NY'] = 'New York'
kota['OR'] = 'Portland'

# Print out some cities
print '-' * 10
print "NY State has: ", kota['NY']
print "OR State has: ", kota['OR']

# Print some states
print '-' * 10
print "Michigan's abbreviation is: ", bagian['Michigan']
print "Florida's abbreviation is: ", bagian['Florida']

# Do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", kota[bagian['Michigan']]
print "Florida has: ", kota[bagian['Florida']]

# Print every state abbreviation
print '-' * 10
for bag, singkatan in bagian.items():
    print "%s is abbreviated %s" % (bag, singkatan)

# Print every city in state
print '-' * 10
for singkatan, k in kota.items():
    print "%s has the city %s" % (singkatan, k)

# Now do both at the same time
print '-' * 10
for bag, singkatan in bagian.items():
    print "%s state is abbreviated %s and has city %s" % (
        bag, singkatan, kota[singkatan]
    )

print '-' * 10
# Safely get a abbreviation by state that might not be there
state = bagian.get('Texas')

if not state:
    print "Sorry, no Texas."

# Get a city with a default value
city = kota.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
