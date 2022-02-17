import opc
import random
from time import sleep

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

def mountain():
    while True:
        #First mountain generation
        for led in range(12):
            leds[303+led]=(0,255,0)
            leds[326-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(10):
            leds[244+led]=(0,255,0)
            leds[265-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(8):
            leds[185+led]=(0,255,0)
            leds[204-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(6):
            leds[126+led]=(0,255,0)
            leds[143-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(4):
            leds[67+led]=(0,255,0)
            leds[82-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(2):
            leds[8+led]=(0,255,0)
            leds[21-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        led =0
        while led < 6:
            leds[327+led]=(255,255,255)
            leds[267+led]=(255,255,255)
            leds[207+led]=(255,255,255)
            leds[147+led]=(255,255,255)
            leds[87+led]=(255,255,255)
            leds[27+led]=(255,255,255)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1          
        #2nd mountain generation
        for led in range(12):
            leds[333+led]=(0,255,0)
            leds[356-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(10):
            leds[274+led]=(0,255,0)
            leds[295-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(8):
            leds[215+led]=(0,255,0)
            leds[234-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(6):
            leds[156+led]=(0,255,0)
            leds[173-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(4):
            leds[97+led]=(0,255,0)
            leds[112-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        for led in range(2):
            leds[38+led]=(0,255,0)
            leds[51-led]=(0,255,0)
            client.put_pixels(leds)
            sleep(0.01)
            led = led +1
        sunRise()
        sleep(1)
        sunDown()
        if counter ==3:
            break
     
def sunRise():
    global counter
    counter = 0  
    while counter <3:
        for led in range(2):
            leds[254+led] = (255,0,0)
            client.put_pixels(leds)
            sleep(0.11)
            led = led + 1
        for led in range(4):
            leds[193+led] = (255,77,0)
            client.put_pixels(leds)
            sleep(.11)
            led = led + 1
        for led in range(6):
            leds[132+led] = (255,103,0)
            client.put_pixels(leds)
            sleep(.11)
            led = led + 1
        for led in range(8):
            leds[71+led] = (255,129,0)
            client.put_pixels(leds)
            sleep(.11)
            led = led + 1
        for led in range(10):
            leds[10+led] = (255,167,0)
            client.put_pixels(leds)
            sleep(.11)
            led = led + 1
#make whole board black to simulate blink            
        for led in range(2):
            leds[254+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(4):
            leds[193+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(6):
            leds[132+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(8):
            leds[71+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(10):
            leds[10+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        counter = counter +1
        
def sunDown():
    global counter
    counter =0
    while counter < 3:
        for led in range(10):
            leds[40+led] = (255,0,0)
            client.put_pixels(leds)
            sleep(.11)
            led = led + 1
        for led in range(8):
            leds[101+led] = (255,77,0)
            client.put_pixels(leds)
            sleep(.11)            
            led = led + 1
        for led in range(6):
            leds[162+led] = (255,103,0)
            client.put_pixels(leds)
            sleep(.11)
            led = led + 1
        for led in range(4):
            leds[223+led] = (255,129,0)
            client.put_pixels(leds)
            sleep(.11)
            led = led + 1           
        for led in range(2):
            leds[284+led] = (255,167,0)
            client.put_pixels(leds)
            sleep(0.11)
            led = led + 1
#make whole board black to simulate blink            
        for led in range(2):
            leds[284+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(4):
            leds[223+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(6):
            leds[162+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(8):
            leds[101+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        for led in range(10):
            leds[40+led] = (0,0,0)
            client.put_pixels(leds)
            led = led + 1
        print(counter)
        counter = counter +1
        
mountain()                                             



        
