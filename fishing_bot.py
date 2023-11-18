# Author : Sébastien Duruz
# Date : 18.11.2023


import pyautogui
import pydirectinput
import os
import keyboard
import time


def check_hook():
    global bot_is_fishing
    global fishing_spot
    global set_hook_button
    try:
        if bot_is_fishing == False:
            try:
                location = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\validate_fishing.PNG')
                pydirectinput.click(x=location.left, y=location.top, clicks=2, interval=0.1)
                print("New item in the inventory !")
            except pyautogui.ImageNotFoundException:
                print("", end="")
            pydirectinput.click(x=fishing_spot[0], y=fishing_spot[1], clicks=2, interval=0.1)
            bot_is_fishing = True
        pyautogui.locateOnScreen(os.getcwd() + '\\assets\\question_mark.PNG', region=[300, 300, 300, 300])
        print('A hooked fish !')
        pydirectinput.click(x=set_hook_button.left, y=set_hook_button.top, clicks=2, interval=0.1)
        time.sleep(5)
        bot_is_fishing = False
    except pyautogui.ImageNotFoundException:
        print("", end="")
    

screen_width = 1920
screen_height = 1080
bot_is_fishing = False
inventory_is_set = False
hook_button_is_set = False
fishing_spot_is_set = False
pause_menu_is_set = False
    
    
print("Setup the bot, please don't move the mouse and make sure FATE client is visible !")
time.sleep(3.0)

while pause_menu_is_set == False:        
    try:
        pause_menu = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\pause_menu.PNG', grayscale=True)
        pydirectinput.click(x=pause_menu.left, y=pause_menu.top, clicks=2, interval=0.1)
        pause_menu_is_set = True
        print("Pause menu set !")
    except pyautogui.ImageNotFoundException:
        print("", end="")

while inventory_is_set == False:      
    try:
        location = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\inventory.PNG', grayscale=True)
        inventory_is_set = True
        print("Inventory set !")
    except pyautogui.ImageNotFoundException:
        pydirectinput.press('i')
 
while fishing_spot_is_set == False:   
    try:
        fishing_spot_helper = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\fishing_spot_helper.PNG', grayscale=True)
        fishing_spot = [fishing_spot_helper.left - 250, fishing_spot_helper.top]
        fishing_spot_is_set = True
        print("Fishing spot set !")
    except pyautogui.ImageNotFoundException:
        print("", end="")


while hook_button_is_set == False:
    try:
        set_hook_button = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\set_hook_button.PNG', grayscale=True)
        pydirectinput.moveTo(set_hook_button.left, set_hook_button.top)
        hook_button_is_set = True
        print("Hook button set !")
    except pyautogui.ImageNotFoundException:
        pydirectinput.click(fishing_spot[0], fishing_spot[1], clicks=2, interval=0.1)
        print("", end="")
            
try:
    set_hook_button = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\set_hook_button.PNG', grayscale=True)
    bot_is_fishing = True
    print("Hook button set !")
except pyautogui.ImageNotFoundException:
    bot_is_fishing = False
    print("", end="")

print("Bot is ready !")
while True:
    check_hook()
        

