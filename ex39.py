# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them.
# this is setup as state abbr and city.
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviate is: ", states['Michigan']
print "Florida's abbreciation is: ", states['Florida']

# do it by using the states then cities dict.
# we have to first search for the state abbr then get the city
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for i, j in states.items():
    print "%s is abbreviated %s" % (i, j)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s states is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', "Does not exist")
print "The city for the state 'TX' is %s" % city