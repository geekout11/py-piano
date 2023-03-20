from pyautogui import *
import pyautogui
import time
import keyboard
import win32api
import win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)  # This pauses the script for 0.05 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:

    # Check each tile
    if pyautogui.pixel(601, 420)[0] == 0:
        click(601, 420)
    if pyautogui.pixel(688, 420)[0] == 0:
        click(688, 420)
    if pyautogui.pixel(772, 420)[0] == 0:
        click(772, 420)
    if pyautogui.pixel(861, 420)[0] == 0:
        click(861, 420)
