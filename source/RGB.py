#####################################################################
# SimVarLights
# Illuminated RGB Addressable Lights based on SimConnect Variables
# by: Diego Vásquez (2020)
# This Software is Open Source under GNU License
# RGB Handler Internal Module
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor
from openrgb.utils import ZoneType

keyb = None
cli = None
keyboard_leds = None
keyboard_zone = None
led_count = None
backColor = None
inopColor = None

#####################################################################
# Initialize OpenRGB Client Connection
# uses OpenRGB-python
def initRGB():
    global keyb
    global cli
    global keyboard_leds
    global keyboard_zone
    global led_count
    cli = OpenRGBClient()
    print(cli)
    keyb = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
    print(keyb)
    keyb.set_mode('direct')
    keyboard_leds = keyb.zones[0].leds
    led_count=len(keyboard_leds)
    keyboard_zone = keyb.zones[0]
    print(f'Keyboard Zone Type: {keyboard_zone.type}')
    #assert keyboard_zone.type == ZoneType.LINEAR
    return keyboard_leds

#####################################################################
# Function for lighting bacground and keys with not-found variables
def light_background(backColorHEX: str, inopColorHEX: str, INOP: int):
    global backColor, inopColor, keyboard_zone, keyboard_leds
    #backColor = RGBColor.fromHEX(backColorHEX)
    #inopColor = RGBColor.fromHEX(inopColorHEX)
    backColor = RGBColor(0,0,32)
    inopColor = RGBColor(127,0,0)
    print(f'Setting global zone {keyboard_zone} background color {backColor} and INOP variables to color {inopColor}.')
    #keyboard_zone.colors = backColor
    #keyboard_zone.update()
    keyboard_zone.set_color(backColor)
    for i in INOP:
        keyboard_leds[i].set_color(inopColor)
                
#####################################################################
# Init Placeholder
def init_lights():
    pass

#####################################################################
# Output Led Info
def write_led_id(column: int, row: int, id: int):
    print(f'Led ID for {column}, {row}: {keyboard_leds[id]}')

#####################################################################
# Light a Led
def light_led(id: int, litColor: RGBColor):
    print(f'Lighting led {id}...')
    keyboard_leds[id].set_color(litColor)

#####################################################################
# Douse a Led
def douse_led(id: int, unlitColor: RGBColor):
    print(f'Dousing led {id}...')
    keyboard_leds[id].set_color(unlitColor)