from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5) # allows a 5 second pause before the key starts getting pressed after running the program

for i in range(1, 100): # edit the second number in order to increase or decrease the amount of times the key is pressed
    keyboard.press('a') # edit the character to change which key is pressed
    keyboard.release('a') # character must be the same as "keyboard.press" above
    time.sleep(1.0) # how many times you want the key pressed per second

