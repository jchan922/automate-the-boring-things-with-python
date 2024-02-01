import os
import time

cwd = f'{os.getcwd()}/chapter-11-files'

print('== Start ==')

print('Step 1: Create file(s) and folder(s)')
exec(open(f'{cwd}/copying-and-movie-files-and-folders.py').read())

print('Step 2: Check for file(s) and folder(s)')
time.sleep(3)

print('Step 3: Delete for file(s) and folder(s)')
exec(open(f'{cwd}/deleting-files.py').read())

print('== Done. ==')