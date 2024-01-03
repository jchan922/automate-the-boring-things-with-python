# Repitition in regex patterns and greedy and non greedy matching

import re

# ? character can match only 0 or 1 times (optional)
batRegex = re.compile(r'Bat(wo)?man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject.group())

matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())

matchObject = batRegex.search('The Adventures of Batwowowoman')
print(matchObject == None)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
matchObject = phoneRegex.search('My number is 555-555-5555. Call me tomorrow.')
print(matchObject.group())

matchObject = phoneRegex.search('My number is 555-5555. Call me tomorrow.')
print(matchObject.group())

# * character can match 0 or more times (optional)
batRegex = re.compile(r'Bat(wo)*man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject.group())

matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())

matchObject = batRegex.search('The Adventures of Batwowowoman')
print(matchObject.group())

# + character must match 1 or more times (required)
batRegex = re.compile(r'Bat(wo)+man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject == None)

matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())

matchObject = batRegex.search('The Adventures of Batwowowoman')
print(matchObject.group())

# escaping
regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))
regex = re.compile(r'(\+\*\?)+')
print(regex.search('I learned about +*?+*?+*?+*?+*? regex syntax'))

# exactly
haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa"'))

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
print(phoneRegex.search('My numbers are 555-555-5555, 111-111-1111, 222-222-2222.'))

# min,max
haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHa"'))
print(haRegex.search('He said "HaHaHaHaHa"'))
print(haRegex.search('He said "HaHaHaHaHaHaHaHaHaHa"'))

# greedy match - longest possible match which is default in python
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))

# non-greedy match - shortest possible match
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890'))
