# Regular expression basics

# without regular expression
def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

print(isPhoneNumber('hello'))
print(isPhoneNumber('510-555-5555'))

message = 'Call me 415-555-1011 tomorrow, or at 15-555-9999'
foundNumber = False
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print(f'Phone number found: {chunk}')
		foundNumber = True
if not foundNumber:
	print('Could not find any phone numbers.')

# with regular expressions
import re

message = 'Call me 415-555-1011 tomorrow, or at 555-555-1011'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search(message)
print(matchObject.group()) # 415-555-1011

message = 'Call me 415-555-1011 tomorrow, or at 555-555-1011'
matchObject = phoneNumRegex.findall(message)
print(phoneNumRegex.findall(message)) # ['415-555-1011', '555-555-1011']