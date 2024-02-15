import logging
import os

cwd = f'{os.getcwd()}/chapter-12-debugging'

logging.basicConfig(filename=f'{cwd}/logging-log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# The 5 debug level
# logging.disable(logging.DEBUG)
# logging.disable(logging.INFO)
# logging.disable(logging.WARNING)
# logging.disable(logging.ERROR)
# logging.disable(logging.CRITICAL) - disable all messages

logging.debug('Start of program')

def factorial(n):
	logging.debug(f'Start of factorial({n})')
	total = 1
	
	for i in range(1, n+1):
		total *= i
		logging.debug(f'i is {i}, total is {total}')

	logging.debug(f'Return value is {total}')
	return total

print(factorial(5))
print('Logs stored in /logging-log.txt')
logging.debug('End of program')