import os
import traceback

try:
	raise Exception('This is the error message')
except:
	cwd = f'{os.getcwd()}/chapter-12-debugging'
	errorFile = open(f'{cwd}/traceback_log.txt', 'a')
	errorFile.write(f'{traceback.format_exc()}\n')
	errorFile.close()
	print('Traceback error written to traceback_log.txt')