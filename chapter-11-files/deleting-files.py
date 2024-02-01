import os
import send2trash
import shutil

cwd = f'{os.getcwd()}/chapter-11-files'

# remove single file
# os.unlink(f'{cwd}/rename.txt')
# os.unlink(f'{cwd}-move/copy.txt')
send2trash.send2trash(f'{cwd}/rename.txt')
send2trash.send2trash(f'{cwd}-move/copy.txt')

# remove directory
# os.rmdir(f'{cwd}-backup')
# shutil.rmtree(f'{cwd}-backup')
send2trash.send2trash(f'{cwd}-backup')
