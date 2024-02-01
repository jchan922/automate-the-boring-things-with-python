import os
import shutil

cwd = f'{os.getcwd()}/chapter-11-files'

# copy a single file
shutil.copy(f'{cwd}/test.txt', f'{cwd}/copy.txt')

# # copy an entire directory
shutil.copytree(cwd, f'{cwd}-backup')

# move a single file
shutil.move(f'{cwd}/copy.txt', f'{cwd}-move')

# rename a single file
shutil.move(f'{cwd}/test.txt', f'{cwd}/rename.txt')
shutil.copy(f'{cwd}/rename.txt', f'{cwd}/test.txt')
