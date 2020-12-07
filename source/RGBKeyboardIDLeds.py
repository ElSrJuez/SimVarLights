##############################################################
# Navigate Keyboard LED Lights for Identification
# Press up/down/left/right to move LED cursos and take note of led 'id' number
# Press ESC to exit.

from openrgb.utils import RGBColor
from pynput.keyboard import Key, Listener
from RGB import *

rows = 6
cols = 22
lit = RGBColor(0,0,255)
unlit = RGBColor(0,0,20)
keyb = None

def on_press(key):
    #print('{0} pressed'.format(
        #key))
    check_key(key)

def on_release(key):
    #print('{0} release'.format(
       # key))
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    global i,row,col,rows,cols,led_count
    if key in [Key.up, Key.down, Key.left, Key.right]:
        douse_led(id = i, unlitColor = unlit) 
        if key is Key.up and row > 0:
            row = row - 1
            i = i - cols
        if key is Key.down and row < rows and (i + cols+1) <= led_count:
            row = row + 1
            i = i + cols
        if key is Key.left and col > 0:
            col = col - 1
            i = i - 1
        if key is Key.right and col < cols and (i + 1)< led_count:
            col = col + 1
            i = i + 1
        write_led_id(column = col, row= row, id = i)
        light_led(id = i, litColor = lit)
        
keyboard_leds = initRGB()
led_count=len(keyboard_leds)
light_background(backColorHEX='#000020',inopColorHEX='#800000',INOP=(1,2,3,4,5))

i = 0
row = 0
col = 0 
write_led_id(column = col, row= row, id = i)
light_led(id = i, litColor = lit)

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()