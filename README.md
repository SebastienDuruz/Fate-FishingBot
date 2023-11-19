# Fishing Bot for the RPG Game FATE
This bot has been tested on the Steam version of **FATE: The Traitor Soul** but should work fine for all FATE games.

## Dependencies
```bash
pip3 install pyautogui pydirectinput opencv-python
```

## Settings

The bot operates optimally when the game is set to Window Mode with a resolution of 1920x1080.

Here is a sample of the changes to be made in the `config.dat` file:
```ini
SCREENWIDTH: 1920
SCREENHEIGHT: 1080
FULLSCREEN: 0
[...]
VSYNC: 0
[...]
1920x1080: 1
[...]
FOV: 70
```

## Issue with the Fishing Spot

If you need to adjust the fishing zone (where you click to start the fishing process), you can modify the values in the `fishing_bot.py` file at **lines 29 and 30**:

```python
fishing_spot_offset_x = 250
fishing_spot_offset_y = 0
```

The values are **subtracted** from the default position.

## Usage

1. Install the required Python libraries.
2. Open the game and move to your fishing spot.
3. Open a terminal in the directory where `fishing_bot.py` is located.
4. Execute the bot using Python 3: `python3.exe .\fishing_bot.py`.
5. When finished, return to the terminal and press `Ctrl-C` to shut down the bot.

## Exemple
[![Video exemple](https://i.ytimg.com/an_webp/GJsejfrqCrg/mqdefault_6s.webp?du=3000&sqp=CLDc6KoG&rs=AOn4CLDlkxULPMeIAab7BDaf4BGKAbVIVQ)](https://www.youtube.com/watch?v=GJsejfrqCrg "FATE - Fishing bot built in Python")