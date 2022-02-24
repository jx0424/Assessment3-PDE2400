import opc
from time import sleep
import random

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

Fcounter = 0
while True:
    randExplosion = random.randint(0,3)
    Fhappened= False
    print(randExplosion)
    randomLoc = random.randint(300,359)
    if Fcounter == 0:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.3)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.3)
            led = led +1
        Fhappened = 1
            
    if Fcounter == 1:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.3)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.3)
            led = led +1
        Fhappened = 1
        
    if Fcounter == 2:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.3)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.3)
            led = led +1
        Fhappened = 1

    if Fcounter ==3:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.3)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.3)
            led = led +1
        Fhappened = 1

    if randExplosion == 0 and Fhappened == 1:
        led=0
        for rows in range(6):
            leds[2+led+rows*60] = (0,255,255)
            leds[302+led-rows*60] = (0,255,255)
            client.put_pixels(leds)
            led=led+1
        sleep(0.5)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)
        sleep(0.8)
        
    if randExplosion == 1 and Fhappened == 1:
        led=0
        for rows in range(6):
            leds[16+led+rows*60] = (0,255,255)
            leds[316+led-rows*60] = (0,255,255)
            client.put_pixels(leds)
            led=led+1
        sleep(0.5)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)
        sleep(0.8)

    if randExplosion == 2 and Fhappened == 1:
        led=0
        for rows in range(6):
            leds[30+led+rows*60] = (0,255,255)
            leds[330+led-rows*60] = (0,255,255)
            client.put_pixels(leds)
            led=led+1
        sleep(0.5)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)
        sleep(0.8)

    if randExplosion == 3 and Fhappened == 1:
        led=0
        for rows in range(6):
            leds[44+led+rows*60] = (0,255,255)
            leds[344+led-rows*60] = (0,255,255)
            client.put_pixels(leds)
            led=led+1
        sleep(0.5)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)
        sleep(0.8) 
        
    Fcounter = Fcounter +1    
    if Fcounter == 4:
        break

