# Author : Sébastien Duruz
# Date : 18.11.2023

"""
Libraries
"""
import pyautogui
import pydirectinput
import os
import keyboard
import threading
import time


"""
Global Variables
"""
bot_is_paused = False
checking_keys = False
main_loop = True
bot_is_fishing = False
inventory_is_set = False
hook_button_is_set = False
fishing_spot_is_set = False
pause_menu_is_set = False

"""
Functions
"""
def check_hook():
    """
    Check the state of the hook and reset when needed
    """
    global bot_is_fishing
    global fishing_spot
    global set_hook_button
    
    try:
        if bot_is_fishing == False:
            # Not currently fishing, check for new item and hook down
            try:
                location = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\validate_fishing.PNG')
                pydirectinput.click(x=location.left, y=location.top, clicks=2, interval=0.1)
                print("New item in the inventory !")
            except pyautogui.ImageNotFoundException:
                print("", end="")
            pydirectinput.click(x=fishing_spot[0], y=fishing_spot[1], clicks=2, interval=0.1)
            bot_is_fishing = True
            
        # Currently fishing, hook up if a hooked fish
        pyautogui.locateOnScreen(os.getcwd() + '\\assets\\question_mark_2.PNG', region=[300, 300, 300, 300])
        print('A hooked fish !')
        pydirectinput.click(x=set_hook_button.left, y=set_hook_button.top, clicks=2, interval=0.1)
        time.sleep(5)
        bot_is_fishing = False
    except pyautogui.ImageNotFoundException:
        print("", end="")
    
def setup_bot():
    """
    Setting up the bot ready for fishing
    """
    global pause_menu_is_set
    global inventory_is_set
    global fishing_spot_is_set
    global hook_button_is_set
    global fishing_spot
    global set_hook_button
    print("Setting up the bot, please don't move the mouse and make sure FATE window is visible !")
    time.sleep(3.0)

    # Close the pause menu if open
    while pause_menu_is_set == False:        
        try:
            pause_menu = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\pause_menu.PNG', grayscale=True)
            pydirectinput.click(x=pause_menu.left, y=pause_menu.top, clicks=2, interval=0.1)
            pause_menu_is_set = True
            print("Pause menu set !")
        except pyautogui.ImageNotFoundException:
            print("", end="")

    # Open the inventory interface
    while inventory_is_set == False:      
        try:
            location = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\inventory.PNG', grayscale=True)
            inventory_is_set = True
            print("Inventory set !")
        except pyautogui.ImageNotFoundException:
            pydirectinput.press('i')
    
    # Find and set the fishing area
    while fishing_spot_is_set == False:   
        try:
            fishing_spot_helper = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\fishing_spot_helper.PNG', grayscale=True)
            fishing_spot = [fishing_spot_helper.left - 250, fishing_spot_helper.top]
            fishing_spot_is_set = True
            print("Fishing spot set !")
        except pyautogui.ImageNotFoundException:
            print("", end="")

    # Find and set the hook button position
    while hook_button_is_set == False:
        try:
            set_hook_button = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\set_hook_button.PNG', grayscale=True)
            hook_button_is_set = True
            print("Hook button set !")
        except pyautogui.ImageNotFoundException:
            pydirectinput.click(fishing_spot[0], fishing_spot[1], clicks=2, interval=0.1)
            print("", end="")
    
    # Check for the current state of the fishing     
    try:
        set_hook_button = pyautogui.locateOnScreen(os.getcwd() + '\\assets\\set_hook_button.PNG', grayscale=True)
        bot_is_fishing = True
        print("Hook button set !")
    except pyautogui.ImageNotFoundException:
        bot_is_fishing = False
        print("", end="")
    
    # Start to check the keyboard inputs
    checking_keys = True
    print("Bot is ready !")

"""
Bot Logics
"""
# Setup the initial bot position
setup_bot()

# Main Loop
while main_loop == True:
    if bot_is_paused == False:
        check_hook()
        

