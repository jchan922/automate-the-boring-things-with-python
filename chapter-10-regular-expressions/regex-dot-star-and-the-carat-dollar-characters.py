# Regex dot-star and the caret dollar characters

import re

# ^ must begin at start of string
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said "Hello!"') == None)

# $ must match at end of string
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!asdfas dfsadf') == None)

# ^ $ both start and end with pattern
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('8971398471938749183759138'))
print(allDigitsRegex.search('8971398471938x749183759138'))

# . wildcard for any character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat say on the flat mat.')) # ['cat', 'hat', 'lat', 'mat']

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat say on the flat mat.')) # [' cat', ' hat', 'flat', ' mat']

# anything - greedy match (by default)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

# anything - greedy match (by default)
greedyAnything = re.compile(r'<(.*)>')
print(greedyAnything.findall('<To serve humans> for dinner.>')) # ['To serve humans> for dinner.']

# anything - non greedy match
nongreedyAnything = re.compile(r'<(.*?)>')
print(nongreedyAnything.findall('<To serve humans> for dinner.>')) # ['To serve humans']

# anything - re.DOTALL
prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL) # match all including whitespace and line breaks
print(dotStar.search(prime))

# anything - re.I
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.search('Al, why does your programming book talk about RoboCop so much?'))
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))
vowelRegex = re.compile(r'[aeiou]', re.I) # ignore case
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))