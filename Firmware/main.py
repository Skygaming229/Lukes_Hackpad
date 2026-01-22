# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# RP2040 (XIAO RP2040) GPIO pins (GP6, GP7, GP0, GP3, GP2, GP4, GP1)
PINS = [board.GP6, board.GP7, board.GP0, board.GP3, board.GP2, board.GP4, board.GP1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define an Alt+F4 macro and map it to all 7 keys
alt_f4 = KC.MACRO(Tap(KC.ALT, KC.F4))

keyboard.keymap = [
    [alt_f4, alt_f4, alt_f4, alt_f4, alt_f4, alt_f4, alt_f4]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
