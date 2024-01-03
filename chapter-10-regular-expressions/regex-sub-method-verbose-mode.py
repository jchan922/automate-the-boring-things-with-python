# Regex sub() method and verbose mode

import re

# Find and replace regex
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret dcouments to Agent Bob.')) # ['Agent Alice', 'Agent Bob']

# sub() - substitute on matches
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret dcouments to Agent Bob.')) # REDACTED gave the secret dcouments to REDACTED.

# sub() - substitute on matches with some parts of original matching string
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret dcouments to Agent Bob.')) # ['A', 'B']
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret dcouments to Agent Bob.')) # Agent A**** gave the secret dcouments to Agent B****..

# Verbose format
verboseRegex = re.compile(r'''
	\d\d\d		# area code
	-			# first dash
	\d\d\d		# first 3 digits
	-			# first dash
	\d\d\d\d	# last 4 digits
	\sx\d{2,4}	# extension like x1234
	''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
