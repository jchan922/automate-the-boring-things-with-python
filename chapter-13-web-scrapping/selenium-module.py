from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

el = browser.find_element(By.CSS_SELECTOR, 'body > div > main > div > ul:nth-child(19) > li:nth-child(2) > a')
print(el)

el.click()
els = browser.find_elements(By.CSS_SELECTOR, 'p')
print(len(els))
print(els[0].text)
