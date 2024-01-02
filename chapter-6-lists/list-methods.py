# list methods

# List.index()
spam = ['hello', 'heyas', 'hi', 'howdy', 'heyas']

try:
	print(spam.index('hello'))
	print(spam.index('heyas')) # returns first in list if dupe
	print(spam.index('does not exist'))
except:
	print('Item does not exist in list')

# List.append()
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam) # ['cat', 'dog', 'bat', 'moose']

# List.insert()
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam) # ['cat', 'chicken', 'dog', 'bat']

# List.remove()
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam) # ['cat', 'rat', 'elephant']

# List.remove()
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['cat', 'elephant', 'bat', 'rat']
spam.sort()
print(spam)

spam = ['cat', 'elephant', 'bat', 'rat']
spam.sort(reverse=True)
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
