# for loops
for i in range(4):
	print(i)

print(list(range(4)))
print(list(range(0, 100, 2)))

supplies = ['pens', 'staples', 'flame-throwers', 'binders']
for i in range (len(supplies)):
	print(f'Index {str(i)} in supplies is: {supplies[i]}')

# standard variable assignment
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(f'Size: {size}') # Size: fat
print(f'Color: {color}') # Color: orange
print(f'Disposition: {disposition}') # Disposition: loud

size, color, disposition = 'skinny', 'black', 'quiet'
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a) # a = 'BBB'
print(b) # b = 'AAA'

# augmented assignment operators
spam = 42
spam += 1
print(spam)