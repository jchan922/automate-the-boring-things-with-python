# Regex character classes and the finall() medthod

import re

# findall()
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.search('555-555-5555, 123-456-7890').group()) # 555-555-5555
print(phoneRegex.findall('555-555-5555, 123-456-7890')) # ['555-555-5555', '123-456-7890']

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall('555-555-5555, 123-456-7890')) # [('555', '555-5555'), ('123', '456-7890')]

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall('555-555-5555, 123-456-7890')) # [('555-555-5555', '555', '555-5555'), ('123-456-7890', '123', '456-7890')]

# character classes
# \d - any numeric digit from 0 to 9
# \D - any character that is not a any numeric digit from 0 to 9
# \w - any letter, numeric digit, or underscore character
# \W - any character that is not a letter, numeric digit, or underscore character
# \s - any space, tab or newline character
# \S - any character that is not a space, tab or newline character

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a swimming, 6 geese a laying, 5 gold rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
lyricsRegex = re.compile(r'\d+\s\w+')
print(lyricsRegex.findall(lyrics))

# custom regex classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.')) # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']
vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall('Robocop eats baby food.')) # ['ea', 'oo']

consonantsRegex = re.compile(r'[^aeiouAEIOU]{2}') # ^ negative character class
print(consonantsRegex.findall('Robocop eats baby food.')) # ['p ', 'ts', ' b', 'by', ' f', 'd.']