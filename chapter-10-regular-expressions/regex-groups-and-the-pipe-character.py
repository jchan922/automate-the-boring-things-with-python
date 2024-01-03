# Regex groups and the pipe character

import re

# basic
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My number is 555-555-5555')
print(matchObject.group()) # 555-555-5555

# groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My number is 555-555-5555')
print(matchObject.group(1)) # 555
print(matchObject.group(2)) # 555-5555

# escaping parens
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My number is (555) 555-5555')
print(matchObject.group()) # (555) 555-5555

# pipe character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject = batRegex.search('Batmobile lost a wheel')
print(matchObject.group()) # Batmobile
print(matchObject.group(1)) # mobile