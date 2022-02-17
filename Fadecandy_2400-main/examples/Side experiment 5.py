import opc
import random
from time import sleep
import asyncio
import threading

leds=[(255,255,255)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

counter = 0
def rainDrop():
    global counter
    while True: 
        leds=[(0,0,0)]*360
        client.put_pixels(leds)
        led=0
        while led <59:
            for rows in range(6):
                leds[led+rows*60] = (0,255,255)
                client.put_pixels(leds)
                led=led+1
                sleep(0.01)
        #print(counter)
        accRain(counter)
        counter = counter +1      
        if counter ==6:
            break


def accRain(counter):
    print(counter)
    #for led in range(60):
    if counter == 0:
        for led in range(60):
            leds[300+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
        
    if counter == 1:
        for led in range(60):
            leds[240+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 2:
        for led in range(60):
            leds[180+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 3:
        for led in range(60):
            leds[120+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 4:
        for led in range(60):
            leds[60+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 5:
        for led in range(60):
            leds[0+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
            
rainDrop()


