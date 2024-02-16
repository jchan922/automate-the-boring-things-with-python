import os
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
status = res.status_code
print(status)
res.raise_for_status()

try:
	badRes = requests.get('https://automatetheboringstuff.com/files/error.txt')
	badRes.raise_for_status()
except:
	print('ERROR: Bad response.')

cwd = f'{os.getcwd()}/chapter-13-web-scrapping'
file = open(f'{cwd}/RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
	file.write(chunk)
file.close()