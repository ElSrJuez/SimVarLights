##############################################################
# Navigate Keyboard LED Lights for Identification
# Press up/down/left/right to move LED cursos and take note of led 'id' number
# Press ESC to exit.

from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor
from pynput.keyboard import Key, Listener

rows = 6
cols = 22
lit = RGBColor(0,0,255)
unlit = RGBColor(0,0,20)
int = None
led_count = None
keyb = None
keyboard_leds = []

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
        douse_led(id = i) 
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
        write_led_id()
        light_led(id = i)
        
def write_led_id():
    print(f'Led ID for {col}, {row}: {keyboard_leds[i]}')

def light_led(id: int):
    print(f'Lighting led {id}...')
    keyboard_leds[id].set_color(lit)

def douse_led(id: int):
    print(f'Dousing led {id}...')
    keyboard_leds[id].set_color(unlit)

cli = OpenRGBClient()
print(cli)
keyb = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
print(keyb)
keyb.set_mode('direct')
keyboard_leds = keyb.zones[0].leds
led_count=len(keyboard_leds)
i = keyboard_leds[0].id
row = 0
col = 0 
write_led_id()
light_led(id = i)

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()