# String formatting

# basic string concatenation
print('Hello' + 'world')

name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'
print('Hello ' + name + ', you are invited to a part at ' + place + ' at ' + time + '. Please bring ' + food + '.')

# string interpolation
print('Hello %s, you are invited to a part at %s at %s. Please bring %s.' % (name, place, time, food))

# string literal w/ f-strings
print(f'Hello ${name}, you are invited to a part at {place} at {time}. Please bring {food}.')