import opc
import random
import time
import colorsys
from datetime import date
from time import sleep 


#---------------------Functions for Animation 1 ----------------------------
def vortex():
    #to first set the led to all white
    leds=[(255,255,255)]*360
    client = opc.Client('localhost:7890')
    client.put_pixels(leds)
    client.put_pixels(leds)

    s = 1.0
    v = 1.0
    #added a counter
    counter = 0
    while True:
        
        for hue in range(360):
            rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v)
            r_float = rgb_fractional[0]
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[2]
            #to randomise the rgb values
            rgb = (r_float*random.randint(100,250), g_float*random.randint(100,250), b_float*random.randint(100,250))
            #to cycle the led board from top left to bottom right
            leds[hue] = rgb
            #to cycle the led from bottom right to top left
            leds[359-hue] = rgb
            client.put_pixels(leds)
            time.sleep(.01)
        counter = counter +1
        print ("Repeated for", counter , "time(s)")
        #when counter reaches 5 aka the led cycled 5 times in the board, break loop
        if counter == 5:
            break

#-----------------------------Fucntions for Animation 2-----------------------------#
#print the letter Y
def printY():
    for rows in range(4):
        leds[123+rows*60]=(255,0,0)
        leds[124+rows*60]=(255,0,0)
        client.put_pixels(leds)
        sleep(0.1)
    leds[62]=(255,0,0)
    leds[65]=(255,0,0)
    client.put_pixels(leds)
    sleep(0.1)

#print the letter E
def printE():
    for rows in range(5):
        leds[68+rows*60]=(255,127,0)
        client.put_pixels(leds)
    led = 0
    while led <3:
        leds[69+led] = (255,127,0)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    led = 0
    while led <3:
        leds[189+led] = (255,127,0)
        client.put_pixels(leds)
        sleep(0.1)
        led = led + 1
    led = 0
    while led <3:
        leds[309+led]=(255,127,0)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    #client.put_pixels(leds)


#print the letter A
def printA():
    for rows in range(4):
        leds[134+rows*60]=(255,255,0)
        client.put_pixels(leds)
        sleep(0.1)
    for rows in range(4):
        leds[137 + rows*60]=(255,255,0)
        client.put_pixels(leds)
        sleep(0.1)
    leds[75]=(255,255,0)
    leds[76]=(255,255,0)
    leds[195]=(255,255,0)
    leds[196]=(255,255,0)
    client.put_pixels(leds)
    sleep(0.1)

#print the letter R
def printR():
    for rows in range(5):
        leds[80+rows*60]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.1)
    led = 0
    while led <2:
        leds[81+led] =(0,255,0)
        client.put_pixels(leds)
        sleep(0.1)
        led = led + 1
    led = 0
    while led < 2:
        leds[201+led] =(0,255,0)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    leds[143] =(0,255,0)
    leds[262] =(0,255,0)
    leds[323] =(0,255,0)
    client.put_pixels(leds)
    sleep(0.1)

#print the 1st number 2
def print_1st2():
    led = 0
    while led < 4:
        leds[86+led]=(0,0,255)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    led = 0
    while led < 4:
        leds[206+led]=(0,0,255)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    led = 0
    while led < 4:
        leds[326+led]=(0,0,255)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    leds[149]=(0,0,255)
    leds[266]=(0,0,255)
    client.put_pixels(leds)
    sleep(0.1)

#print the number 0
def print0():
    for rows in range(5):
        leds[92+rows*60]=(75,0,130)
        client.put_pixels(leds)    
    leds[93]=(75,0,130)
    leds[94]=(75,0,130)
    for rows in range(5):
        leds[95+rows*60]=(75,0,130)
        client.put_pixels(leds)    
    leds[333]=(75,0,130)
    leds[334]=(75,0,130)
    #client.put_pixels(leds)
    sleep(0.1)

#print the 2nd number 2
def print_2nd2():
    led = 0
    while led < 4:
        leds[98+led]=(148,0,211)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    led = 0
    while led < 4:
        leds[218+led]=(148,0,211)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    led = 0
    while led < 4:
        leds[338+led]=(148,0,211)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    leds[161]=(148,0,211)
    leds[278]=(148,0,211)
    client.put_pixels(leds)
    sleep(0.1)

#print the 3rd number 2
def print_3rd2():
    led = 0
    while led < 4:
        leds[104+led]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    led = 0
    while led < 4:
        leds[224+led]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    led = 0
    while led < 4:
        leds[344+led]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1
    leds[167]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    leds[284]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    client.put_pixels(leds)
    sleep(0.1)

#print smiley face
def printSmiley():
    for rows in range (5):
        leds[109+rows*60]=(225,255,0)
        leds[115+rows*60]=(225,255,0)
        client.put_pixels(leds)
        sleep(0.1)
        
    led = 0
    while led <= 5:
        leds[110+led] = (225,255,0)
        leds[349+led] = (225,255,0)
        client.put_pixels(leds)
        led=led+1
        sleep(0.1)
    led=0
    while led <3:
        leds[231+led] = (225,255,0)
        leds[291+led] = (0,0,255)
        client.put_pixels(leds)
        led = led +1
        sleep (0.1)
    leds[170]= (225,255,0)  
    leds[172]= (225,255,0)  
    leds[174]= (225,255,0)
    leds[290]= (225,255,0)  
    leds[294]= (225,255,0)
    leds[230] = (0,0,255)
    leds[173] = (0,0,255)
    leds[171] = (0,0,255)
    leds[234] = (0,0,255)
    client.put_pixels(leds)
    sleep(0.1)

def printSad():
    for rows in range (5):
        leds[109+rows*60]=(225,255,0)
        leds[115+rows*60]=(225,255,0)
        client.put_pixels(leds)
        sleep(0.1)
        
    led = 0
    while led <= 5:
        leds[110+led] = (225,255,0)
        leds[349+led] = (225,255,0)
        client.put_pixels(leds)
        led=led+1
        sleep(0.1)
    led=0
    while led <3:
        leds[231+led] = (255,0,0)
        leds[291+led] = (225,255,0)
        client.put_pixels(leds)
        led = led +1
        sleep (0.1)
    leds[170]= (225,255,0)  
    leds[172]= (225,255,0)  
    leds[174]= (225,255,0)
    leds[290]= (255,0,0)  
    leds[294]= (255,0,0)
    leds[230] = (225,255,0)
    leds[173] = (255,0,0)
    leds[171] = (255,0,0)
    leds[234] = (225,255,0)
    client.put_pixels(leds)
    sleep(0.1)

#call function
#vortex()
if __name__== "__main__":
    leds=[(255,255,255)]*360
    client = opc.Client('localhost:7890')
    client.put_pixels(leds)
    client.put_pixels(leds)
    
    led = 0
    while led<60: #scroll through all rows at the same time
        for rows in range(6):
            leds[led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        sleep(.1)
        led = led + 1

    printY()
    printE()
    printA()
    printR()
    print_1st2()
    print0()
    print_2nd2()
    print_3rd2()
    printSad()

