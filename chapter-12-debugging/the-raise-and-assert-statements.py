# RAISE
def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('symbol needs to be a string of length 1')
	if (width < 2) or (height < 2):
		raise Exception('width or height needs to be greater than 1')


	print(symbol * width)

	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)

	print(symbol * width)

boxPrint('*', 15, 5)
# ***************
# *             *
# *             *
# *             *
# ***************

boxPrint('o', 15, 5)
# ooooooooooooooo
# o             o
# o             o
# o             o
# ooooooooooooooo

# test exceptions
# boxPrint('**', 15, 5)
# boxPrint('*', 1, 1)

# ASSERT
market_2nd = {'ns' : 'green', 'ew': 'red'}

def switchLights(intersection):
	for key in intersection.keys():
		if intersection[key] == 'green':
			intersection[key] = 'yellow'
		elif intersection[key] == 'yellow':
			intersection[key] = 'red'
		elif intersection[key] == 'red':
			intersection[key] = 'green'
	assert 'red' in intersection.values(), f'Neither light is red! {str(intersection)}'

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)