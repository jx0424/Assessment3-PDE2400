import opc
import random
import time
import colorsys

leds=[(255,255,255)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

s = 1.0
v = 1.0

while True:
    for hue in range(360):
        rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v)
        r_float = rgb_fractional[0]
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]
        rgb = (r_float*255, g_float*255, b_float*255)
        leds[hue] = rgb
        leds[359-hue] = rgb
        client.put_pixels(leds)
        time.sleep(.01)
    
        

