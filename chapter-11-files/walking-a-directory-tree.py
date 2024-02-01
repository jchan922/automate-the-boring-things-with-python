import os

cwd = f'{os.getcwd()}'

for folderName, subfolders, filenames in os.walk(cwd):
	if folderName.__contains__('/.git'):
		break

	print(f'Folder: {folderName}')
	print(f'Subfolders: {subfolders}')
	print(f'Filenames: {filenames}')
	print()

