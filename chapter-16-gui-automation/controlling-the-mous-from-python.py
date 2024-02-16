import pyautogui

width, height = pyautogui.size()
print(width)
print(height)

x, y = pyautogui.position()
print(x)
print(y)

pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10, duration=1.5)
pyautogui.moveTo(10,10, duration=1.5)
pyautogui.moveRel(20,0)
pyautogui.moveRel(200,0)
pyautogui.moveTo(200,0, duration=2)
pyautogui.moveRel(0,-100)
pyautogui.moveRel(0,-100, duration=1)
pyautogui.position()
pyautogui.click(339,38)
pyautogui.click()