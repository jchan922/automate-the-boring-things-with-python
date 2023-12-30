# while statement
spam = 0
while spam < 5:
	print('Hello World')
	spam = spam + 1

name = ''
while True:
	print('Please type your name.')
	name = input()
	if name.lower() == 'your name':
		break
print('Thank you!')

jam = 0
while jam < 5:
	jam = jam + 1
	if jam == 3:
		continue
	print(f'jam is {str(jam)}')