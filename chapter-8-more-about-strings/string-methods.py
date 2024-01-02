# String methods

# String.upper()
spam = 'Hello world!'
print(spam.upper())

# String.lower()
print(spam.lower())

# String.isupper()
spam = 'HELLO WORLD'
print(spam.isupper())
print(''.isupper())

# String.islower()
spam = 'hello world'
print(spam.islower())
print(''.islower())

# String.isalpha() - numbers only
print('hello'.isalpha())
print('hello123'.isalpha())

# String.isalnum() - letters and numbers only
print('hello'.isalpha())
print('hello123'.isalnum())

# String.isdecimal() - numbers only
print('123432342'.isdecimal())

# String.isspace() - whitespace only
print('      '.isspace())

# String.istitle() - titlecase only
print('Hello There'.istitle())

# String.startswith()
print('Hello World!'.startswith('H'))

# String.endswith()
print('Hello World!'.endswith('orld!'))

# String.join()
print(', '.join(['cats', 'rats', 'bats'])) # cats, rats, bats
print(''.join(['cats', 'rats', 'bats'])) # catsratsbats

# String.split()
print('My name is Simon'.split()) # ['My', 'name', 'is', 'Simon']
print('My name is Simon'.split('m')) # ['My na', 'e is Si', 'on']

# String.rjust()
print('Hello'.rjust(10))

# String.ljust()
print('Hello'.ljust(20, '*')) # Hello***************

# String.center()
print('Hello'.center(20, '=')) # =======Hello========

# String.strip() - all white space
spam = 'Hello'.rjust(10)
print(spam.strip())
# String.lstrip()
# String.rstrip()

# String.replace()
spam = 'Hello there!'
print(spam.replace('e', 'XYZ')) # HXYZllo thXYZrXYZ!

