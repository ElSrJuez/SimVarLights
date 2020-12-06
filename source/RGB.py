from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor

def initRGB():
    cli = OpenRGBClient()
    print(cli)
    keyb = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
    print(keyb)
    keyb.set_mode('direct')
    keyb.zones[zonenumber].resize(ledstripsize)
print(mobo.zones[zonenumber])

myLeds = mobo.zones[zonenumber].leds
for i in myLeds:
    i.set_color(red)

step = ((maxperf-minperf)/len(myLeds))

while True: 
    procperf = winstats.get_perf_data(r'\Processor Information(_Total)\% Processor Performance',fmts='double',delay=1000)
    j = int((procperf[0] - minperf) / step)
    print(j, procperf)
    for i in range(len(myLeds)):
        if i <= j:
            myLeds[i].set_color(red)
        else:
            myLeds[i].set_color(blue)