# functions
def hello():
	print('Howdy!')
	print('Howdy!!!!')
	print('Hello there.')

hello()

def hello(name):
	print(f'Howdy! {name}')

hello('Alice')
hello('Bob')

def plusOne(num):
	return num + 1

newNumber = plusOne(5)
print(newNumber)

print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep='ABC')