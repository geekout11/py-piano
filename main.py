from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# 601, 650
# 688, 650
# 772, 650
# 861, 650

def click(x, y):
    win32api.SetCursorPos((x,y))
    # Click then release
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    # Check each tile
    if pyautogui.pixel(601, 650) [0] == 0:
        click(601, 650)
    if pyautogui.pixel(688, 650) [0] == 0:
        click(688, 650)
    if pyautogui.pixel(772, 650) [0] == 0:
        click(772, 650)
    if pyautogui.pixel(861, 650) [0] == 0:
        click(861, 650)