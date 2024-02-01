import os

file = open(f'{os.getcwd()}/chapter-11-files/test.txt')
file.read()
file.close()

file = open(f'{os.getcwd()}/chapter-11-files/test.txt')
print(file.read())
# Hello World!
# Hello Again!!
file.close()

file = open(f'{os.getcwd()}/chapter-11-files/test.txt')
print(file.readlines())
# ['Hello World!\n', 'Hello Again!!']
file.close()

# WRITE MODE
file = open(f'{os.getcwd()}/chapter-11-files/write.txt', 'w')
file.write('Write!!!!!!\n')
file.write('Write!!!!!!\n')
file.write('Write!!!!!!\n')
file.close()

# APPEND MODE
file = open(f'{os.getcwd()}/chapter-11-files/write.txt', 'a')
file.write('Append!!!!!!\n')
file.write('Append!!!!!!\n')
file.write('Append!!!!!!\n')
file.close()