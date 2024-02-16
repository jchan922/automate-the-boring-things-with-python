import os
import pyautogui

cwd = f'{os.getcwd()}/chapter-16-gui-automation'

image = pyautogui.screenshot()
image.save(f'{cwd}/screenshot-example.png')