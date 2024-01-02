# Advanced string syntax

# Single and double quotes 
print("That is Alice's Cat") # That is Alice's Cat

# OR escaped character(s)
print('Say hi to Bob\'s mother') # Say hi to Bob's mother
print('Hello there!\nHow are you?\nI\'m fine.') # multi line

# Raw string
print(r'Hello')
print(r'That is Carol\'s cat') # That is Carol\'s cat

# Multiline strings
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.	
Sincerely,
Bob''')

print('''
	Dear Alice,
		Eve's cat has been arrested for catnapping, cat burglary, and extortion.	
	Sincerely,
	Bob
''')

# Methods similar to lists
name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)
print('xxx' in name)
for letter in name:
	print(letter)
