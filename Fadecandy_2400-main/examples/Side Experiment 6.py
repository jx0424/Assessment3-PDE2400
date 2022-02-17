import opc
import random
from time import sleep

leds=[(255,255,255)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

while True:
    for led in range(29):
        leds[300+led]=(0,255,0)
        leds[359-led]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.01)
        led = led +1
    for led in range(27):
        leds[241+led]=(0,255,0)
        leds[298-led]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.01)
        led = led +1
    for led in range(25):
        leds[182+led]=(0,255,0)
        leds[237-led]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.01)
        led = led +1
    for led in range(23):
        leds[123+led]=(0,255,0)
        leds[176-led]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.01)
        led = led +1
    for led in range(21):
        leds[64+led]=(0,255,0)
        leds[115-led]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.01)
        led = led +1
    for led in range(19):
        leds[5+led]=(0,255,0)
        leds[54-led]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.01)
        led = led +1






        
