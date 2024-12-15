from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController, Button

keyboard = Controller()
mouse = MouseController()

def tap_action():
    keyboard.press('x')
    keyboard.release('x')

def hold_action():
    keyboard.press('x')

def release_action():
    keyboard.release('x')
