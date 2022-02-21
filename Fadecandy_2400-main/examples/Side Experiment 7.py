import opc
from time import sleep
import random

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

Fcounter = 0
while True:
    randomLoc = random.randint(300,359)
    if Fcounter == 1:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.5)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.5)
            led = led +1
        leds[124]=(0,0,255)
        leds[125]=(0,0,255)
        leds[184]=(0,0,255)
        leds[185]=(0,0,255)
        leds[63]=(0,0,255)
        leds[2]=(0,0,255)
        leds[243]=(0,0,255)
        leds[302]=(0,0,255)
        leds[246]=(0,0,255)
        leds[307]=(0,0,255)
        leds[66]=(0,0,255)
        leds[7]=(0,0,255)
        client.put_pixels(leds)
        sleep(1)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)
        
    if Fcounter == 2:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.5)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.5)
            led = led +1
        leds[138]=(0,0,255)
        leds[139]=(0,0,255)
        leds[198]=(0,0,255)
        leds[199]=(0,0,255)
        leds[77]=(0,0,255)
        leds[16]=(0,0,255)
        leds[257]=(0,0,255)
        leds[316]=(0,0,255)
        leds[260]=(0,0,255)
        leds[321]=(0,0,255)
        leds[80]=(0,0,255)
        leds[21]=(0,0,255)
        client.put_pixels(leds)
        sleep(1)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)

    if Fcounter == 2:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.5)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.5)
            led = led +1
        leds[152]=(0,0,255)
        leds[153]=(0,0,255)
        leds[212]=(0,0,255)
        leds[213]=(0,0,255)
        leds[91]=(0,0,255)
        leds[30]=(0,0,255)
        leds[271]=(0,0,255)
        leds[330]=(0,0,255)
        leds[274]=(0,0,255)
        leds[335]=(0,0,255)
        leds[94]=(0,0,255)
        leds[35]=(0,0,255)
        client.put_pixels(leds)
        sleep(1)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)
        
    if Fcounter ==3:
        for led in range(5):
            leds[randomLoc-led*60]=(255,0,255)
            client.put_pixels(leds)
            sleep(0.5)
            leds[randomLoc-led*60]=(0,0,0)
            client.put_pixels(leds)
            sleep(0.5)
            led = led +1
        leds[166]=(0,0,255)
        leds[167]=(0,0,255)
        leds[226]=(0,0,255)
        leds[227]=(0,0,255)
        leds[105]=(0,0,255)
        leds[44]=(0,0,255)
        leds[285]=(0,0,255)
        leds[344]=(0,0,255)
        leds[288]=(0,0,255)
        leds[349]=(0,0,255)
        leds[108]=(0,0,255)
        leds[49]=(0,0,255)
        client.put_pixels(leds)
        sleep(1)
        leds= [(0,0,0)]*360
        client.put_pixels(leds)
        
    Fcounter = Fcounter +1    
    if Fcounter == 4:
        break

