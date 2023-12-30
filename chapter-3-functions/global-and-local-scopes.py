# global and local scopes

spam = 42 # global variable

def eggs():
	spam = 42 # local variable

print('Some code here.') # global variable
print('Some more code.') # global variable

def spam():
	global eggs
	eggs = 'Hello'
	print(eggs)

eggs = 42
spam()
print(eggs) # Output 'Hello'
eggs = 42 # resets variable eggs
print(eggs) # Output 42