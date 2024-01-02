# lists and strings similarities

print(list('Hello'))

name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)
print('xxx' in name)
for letter in name:
	print(letter)

name = 'Zophie a cat'
newName = f'{name[0:7]} the {name[8:12]}'
print(newName)

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese) # references the same list
print(spam) # references the same list

# list references
def eggs(list):
	list.append('Hello')
spam = [1,2,3]
eggs(spam)
print(spam) # [1, 2, 3, 'Hello']

# deep copy of original reference
import copy
spam = ['A','B','C','D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(f'Cheese list: {cheese}')
print(f'Spam list: {spam}')

spam = ['apples']