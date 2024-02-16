import pyperclip
import sys
import webbrowser

# webbrowser.open('https://automatetheboringstuff.com')

print(sys.argv)

# Check if command line agruments were passed
if len(sys.argv) > 1:
	address = (''.join(sys.argv[1:]))
else:
	address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/20700 Avalon Blvd, Carson, CA 90746')