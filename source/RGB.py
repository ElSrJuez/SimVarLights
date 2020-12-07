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

def light_background(backColorHEX: str, inopColorHEX: str, INOP: int):
    global backColor, inopColor, keyboard_zone, keyboard_leds
    #backColor = RGBColor.fromHEX(backColorHEX)
    #inopColor = RGBColor.fromHEX(inopColorHEX)
    backColor = RGBColor(0,0,32)
    inopColor = RGBColor(127,0,0)
    keyboard_zone
    print(f'Setting global zone {keyboard_zone} background color {backColor} and INOP variables to {inopColor}.')
    keyboard_zone.colors = backColor
    keyboard_zone.update()
    for i in INOP:
        keyboard_leds[i].set_color(inopColor)
    
            
def init_lights():
    pass

initRGB()
light_background(backColorHEX='#000020',inopColorHEX='#800000',INOP=(1,2,3,4,5))