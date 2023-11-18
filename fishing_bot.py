# Author : Sébastien Duruz
# Date : 18.11.2023


import pyautogui
import os
import keyboard

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(os.getcwd() + '/screenshot.png')


while True:
    if keyboard.read_key() == "y":
        take_screenshot()


