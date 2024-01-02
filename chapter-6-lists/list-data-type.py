# list data type

['cat', 'bat', 'rat', 'elephant']
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0][1])
print(spam[1][4])

# negative list index
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1]) # elephant
print(spam[-2]) # rat
print(f'The {spam[-1]} is afraid of the {spam[-3]}')

# insert at index
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[1:3]) # new array ['bat', 'rat']
spam = 'Hello'
spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam) # [10, 'Hello', 30]

# list.slice()
spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print(spam) # [10, 'CAT', 'DOG', 'MOUSE']

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2]) # ['cat', 'bat']
print(spam[1:]) # ['bat', 'rat', 'elephant']

# del
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam) # ['cat', 'bat', 'elephant']

# misc
print(len([1,2,3]))
print([1,2,3] + [4,5,6]) # [1,2,3,4,5,6]
print([1,2,3] * 3) # [1,2,3,1,2,3,1,2,3]
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print(42 in ['hello', 'hi', 'howdy', 'heyas'])
print('howdy' not in ['hello', 'hi', 'howdy', 'heyas'])