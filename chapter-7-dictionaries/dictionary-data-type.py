# dictionary data type

dict = {
	'size': 'fat',
	'color': 'gray',
	'disposition': 'loud'
}
print(dict['size'])
print(f'My cat has {dict['color']} fur.')

eggs = {
	'name': 'Zophie',
	'species': 'cat',
	'age': 8
}
print('name' in eggs)
print('name' not in eggs)

# Dict.keys()
eggs = {
	'name': 'Zophie',
	'species': 'cat',
	'age': 8
}
print(eggs.keys())
for key in eggs.keys():
	print(key)

# Dict.values()
eggs = {
	'name': 'Zophie',
	'species': 'cat',
	'age': 8
}
print(eggs.values())
for value in eggs.values():
	print(value)
	
# Dict.items()
eggs = {
	'name': 'Zophie',
	'species': 'cat',
	'age': 8
}
print(eggs.items())
for item in eggs.items():
	print(item) # returns a tuple
for key, value in eggs.items():
	print(key, value)

# Dict.get()
eggs = {
	'name': 'Zophie',
	'species': 'cat',
	'age': 8
}
print(eggs.get('age', 0))
print(eggs.get('color', ''))

picnicItems = {
	'apples': 5,
	'cups': 2
}
print(f'I am bringing {str(picnicItems.get('napkins', 0))} to the picnic')

# Looping
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
	count.setdefault(character, 0)
	count[character] += 1

pprint.pprint(count)
text = pprint.pformat(count)
print(text)