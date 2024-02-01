import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))	
# folder1/folder2/folder3/file.png

print(os.sep)
# /

print(os.getcwd())
# /Users/justinchan/Desktop/Repos/automate-the-boring-things-with-python

print(os.path.abspath('test.txt'))
# /Users/justinchan/Desktop/Repos/automate-the-boring-things-with-python/test.txt

print(os.path.isabs('test.txt'))
# False

print(os.path.dirname('/Users/justinchan/Desktop/Repos/automate-the-boring-things-with-python/test.txt'))
# /Users/justinchan/Desktop/Repos/automate-the-boring-things-with-python

print(os.path.basename('/Users/justinchan/Desktop/Repos/automate-the-boring-things-with-python/test.txt'))
# test.txt