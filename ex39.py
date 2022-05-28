# list revisit
things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things)

# practicing dictionary
stuff = {
	'name' : 'Ratul Sharker',
	'age' : 39,
	'height' : '5 feet 7.5 inch'
}

print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

# adding new items to dictionary
stuff[1] = "One"
stuff[2] = "Two"

print(stuff)

# removing items from dictionary
del stuff[1]
del stuff[2]

print(stuff)

# More exersicing on dictionary
states = {
	'oregon': 'or',
	'florida' : 'fl',
	'california' : 'ca',
	'new york' : 'ny',
	'michigan' : 'mi'
}

cities = {
	'ca' : 'san fransisco',
	'mi' : 'detroit',
	'fl' : 'jacksonville'
}

cities['ny'] = 'new york'
cities['or'] = 'portland'

# print some cities
print('-' * 10)

print('ny state has: ', cities['ny'])
print('or state has: ', cities['or'])

# print some states
print('-' * 10)

print("michigans abbreviation is : ", states['michigan'])
print("florida's abbreviation is : ", states['florida'])

# print some cities by using the state name
print('-' * 10)

print("michigan has : ", cities[states['michigan']])
print("florida has : ", cities[states['florida']])

# print every state abbreviation
print('-' * 10)
for state, abbr in list(states.items()):
	print(f"{state} abbreviation is {abbr}")

# print every city in state
print('-' * 10)
for state, abbr in list(states.items()):
	print(f"{state} has city {cities[abbr]}")

# unsafely get abbreviation by state that might not be there
print('-' * 10)
try:
	state = states['texas']
except KeyError as err:
	print("KeyError {err}")

# safely get abbreviation by state that might not exists
print('-' * 10)
state = states.get('texas')

if state is None:
	print("Nothing found with key 'texas'")

# get a cities of non-existing state
city = cities.get('tx', 'No cities for texas')
print(city)
