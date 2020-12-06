from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor

from pynput import keyboard


def initRGB():
    cli = OpenRGBClient()
    print(cli)
    keyb = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
    print(keyb)
    keyb.set_mode('direct')
    keyboard_leds = keyb.zones[0].leds
    i = leds[0].id 
    while True:
        # The event listener will be running in this block
        with keyboard.Events() as events:
            # Block at most one second
            event = events.get(1.0)
            if event is None:
                print('You did not press a key within one second')
            else:
                print('Received event {}'.format(event))
            

