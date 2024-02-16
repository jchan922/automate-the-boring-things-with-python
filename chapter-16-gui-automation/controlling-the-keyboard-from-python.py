import pyautogui

# pyautogui.click; pyautogui.typewrite('Hello World', interval=0.2)
# pyautogui.click; pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)
pyautogui.press('aa')
pyautogui.hotkey('command', 'a')

print(pyautogui.KEYBOARD_KEYS)