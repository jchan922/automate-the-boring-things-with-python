import bs4
import requests

url='https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.129'}
res = requests.get(url, headers=headers)
res.raise_for_status()
print(res.status_code)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
els = soup.select('#productTitle')
print(els)

