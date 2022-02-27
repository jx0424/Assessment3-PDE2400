import tkinter as tk
import numpy
import opc
import random
import time
import colorsys
from time import sleep 

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

def Welcome(): 
#----------------Letter W----------------------------#
    for rows in range(5):
        leds[62+rows*60]=(148,0,211)
        leds[66+rows*60]=(148,0,211)
        client.put_pixels(leds)
        sleep(0.1)
    led=0
    for rows in range(3):
        leds[302+led-rows*60]=(148,0,211)
        leds[306-led-rows*60]=(148,0,211)
        client.put_pixels(leds)
        led=led+1
        sleep(0.1)

#--------------Letter E-----------------------------#
    for led in range(5):
        leds[69+led]=(75,0,130)
        leds[189+led]=(75,0,130)
        leds[309+led]=(75,0,130)
        client.put_pixels(leds)
        led=led+1
        sleep(0.1)
    for rows in range(5):
        leds[69+rows*60]=(75,0,130)
        client.put_pixels(leds)
        sleep(0.1)
        
#-------------Letter L------------------------------#
    for rows in range(5):
        leds[76+rows*60]=(0, 0, 255)	
        client.put_pixels(leds)
        sleep(0.1)
    for led in range(5):
        leds[316+led]=(0, 0, 255)
        client.put_pixels(leds)
        sleep(0.1)

#-------------------Letter C------------------------#
    for rows in range(5):
        leds[83+rows*60]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.1)
    for led in range(5):
        leds[83+led]=(0,255,0)
        leds[323+led]=(0,255,0)
        client.put_pixels(leds)
        sleep(0.1)

#-----------------Letter O--------------------------#
    for rows in range(5):
        leds[90+rows*60]=(255,255,0)
        leds[94+rows*60]=(255,255,0)    
        client.put_pixels(leds)
        sleep(0.1)
    for led in range(5):
        leds[90+led]=(255,255,0)
        leds[330+led]=(255,255,0)
        client.put_pixels(leds)
        sleep(0.1)

#---------------Letter M---------------------------#
    for rows in range(5):
        leds[97+rows*60]=(255,127,0)
        leds[101+rows*60]=(255,127,0)    
        client.put_pixels(leds)
        sleep(0.1)
    led=0
    for rows in range(3):
        leds[97+led+rows*60]=(255,127,0)
        leds[101-led+rows*60]=(255,127,0)
        client.put_pixels(leds)
        led=led+1
        sleep(0.1)

#-------------Letter 2ndE--------------------------#
    for led in range(5):
        leds[104+led]=(255,0,0)
        leds[224+led]=(255,0,0)
        leds[344+led]=(255,0,0)
        client.put_pixels(leds)
        led=led+1
        sleep(0.1)
    for rows in range(5):
        leds[104+rows*60]=(255,0,0)
        client.put_pixels(leds)
        sleep(0.1)

#----------- 1st !-------------------------------#
    for rows in range(3):
        leds[111+rows*60]=(255,255,255)
        client.put_pixels(leds)
        sleep(0.1)
    leds[351]=(255,255,255)
    client.put_pixels(leds)
    sleep(0.1)    

#----------- 2nd !-------------------------------#
    for rows in range(3):
        leds[114+rows*60]=(155,155,155)
        client.put_pixels(leds)
        sleep(0.1)
    leds[354]=(155,155,155)
    client.put_pixels(leds)
    sleep(0.1)    

#----------- 3rd !-------------------------------#
    for rows in range(3):
        leds[117+rows*60]=(55,55,55)
        client.put_pixels(leds)
        sleep(0.1)
    leds[357]=(55,55,55)
    client.put_pixels(leds)
    sleep(0.1)    


#---------------------Functions for Animation 1(Vortex)----------------------------
def vortex():
#To first set the led to all white
    leds=[(0,0,0)]*360
    client.put_pixels(leds)   
#-----------------------rgb value converter---------------------------------------   
#maximum brightness of colour
    s = 1.0
    v = 1.0
    pixels =[]
#added a counter
    counter = 0
    while counter <3:       
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
        #if counter == 3:
          #  break
    if counter ==3:
        led = 0
        while led<60:
            for rows in range(6):
                leds[led + rows*60] = (0,0,0)
            client.put_pixels(leds)
            led = led +1
        sleep(0.1)        
        for hue in range(360): # shift through the entire colour spectrum
            rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) #colorsys returns floats between 0 and 1
            r_float = rgb_fractional[0] #extract said floating point numbers
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[2]
            rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
            pixels.append(rgb)
        if counter < 6:
            for i in range(360):
                client.put_pixels(pixels)
                pixels = numpy.roll(pixels,3) #roll by 3 because func seems to not care about tuples and rolled elements from them by 1.
                sleep(0.0002) #speed of animation controlled through this
    led = 0
    while led<60:
        for rows in range(6):
            leds[led + rows*60] = (0,0,0)
            client.put_pixels(leds)
            led = led +1
   
#-----------------------------Fucntions for Animation 2 (Year 2022)-----------------------------#      
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
        leds[189+led] = (255,127,0)
        leds[309+led]=(255,127,0)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1

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
    for led in range(2):
        leds[75+led]=(255,255,0)
        leds[195+led]=(255,255,0)
        client.put_pixels(leds)
        sleep(0.1)
        led = led +1

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
    for led in range(7):
        leds[109+led]=(255,255,0)
        leds[169+led]=(255,255,0)
        leds[229+led]=(255,255,0)
        leds[289+led]=(255,255,0)
        leds[349+led]=(255,255,0)
        client.put_pixels(leds)
        sleep(0.1)
    led=0
    while led <3:
        leds[291+led] = (0,0,255)
        client.put_pixels(leds)
        led = led +1
        sleep (0.1)
    leds[230] = (0,0,255)
    leds[173] = (0,0,255)
    leds[171] = (0,0,255)
    leds[234] = (0,0,255)
    client.put_pixels(leds)
    sleep(0.1)

#Print Sad Face 
def printSad():
    for led in range(7):
        leds[109+led]=(255,255,0)
        leds[169+led]=(255,255,0)
        leds[229+led]=(255,255,0)
        leds[289+led]=(255,255,0)
        leds[349+led]=(255,255,0)
        client.put_pixels(leds)
        sleep(0.1)
    led=0
    while led <3:
        leds[231+led] = (255,0,0)
        client.put_pixels(leds)
        led = led +1
        sleep (0.1)
    leds[173] = (255,0,0)
    leds[171] = (255,0,0)   
    leds[290]= (255,0,0)  
    leds[294]= (255,0,0)
    client.put_pixels(leds)
    sleep(0.1)

def Year2022Sad():
    led = 0
    while led<60:
        for rows in range(6):
            leds[led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        led = led +1
    sleep(0.1)
    printY()
    printE()
    printA()
    printR()
    print_1st2()
    print0()
    print_2nd2()
    print_3rd2()
    printSad()
        
def Year2022Happy():
    led = 0
    while led<60:
        for rows in range(6):
            leds[led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        led = led +1
    sleep(0.1)
    printY()
    printE()
    printA()
    printR()
    print_1st2()
    print0()
    print_2nd2()
    print_3rd2()
    printSmiley()
    led = 0
            
def year2022():
    list1=['s','S','sad','Sad','SAD']
    list2=['h','H','happy','Happy','HAPPY']
    happyOrsad= str(input("How is your 2022 so far, Happy or Sad?: "))
    while happyOrsad not in list1 or happyOrsad not in list2:
        if happyOrsad in list1:
            Year2022Sad()
            led = 0
            while led<60:
                for rows in range(6):
                    leds[led + rows*60] = (0,0,0)
                    client.put_pixels(leds)
                led = led +1   
            break
        elif happyOrsad in list2:
            Year2022Happy()
            led = 0
            while led<60:
                for rows in range(6):
                    leds[led + rows*60] = (0,0,0)
                    client.put_pixels(leds)
                led = led +1               
            break
        else:
            happyOrsad = input("Please type in an appropriate input: " )
        

#-------------Function for Animation 3(RainDrop)--------------------
def rainDrop():
    global counter
    counter =0
    flood = 0
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
        flood = accRain(counter,flood)
        counter = counter +1      
        if counter ==6:
            break
    led = 0
    while led<60:
        for rows in range(6):
            leds[led + rows*60] = (0,0,0)
            client.put_pixels(leds)
            led = led +1
            
def accRain(counter,flood):
    leds = 0
    if counter == 0:
        leds=[(0,0,0)]*360
        client.put_pixels(leds)
        for led in range(60):
            leds[300+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
        
    if counter == 1:
        leds = flood
        client.put_pixels(leds)
        for led in range(60):
            leds[240+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 2:
        leds = flood
        client.put_pixels(leds)
        for led in range(60):
            leds[180+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 3:
        leds = flood
        client.put_pixels(leds)
        for led in range(60):
            leds[120+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 4:
        leds = flood
        client.put_pixels(leds)
        for led in range(60):
            leds[60+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    if counter == 5:
        leds = flood
        client.put_pixels(leds)
        for led in range(60):
            leds[0+led]= (0,255,255)
            client.put_pixels(leds)
            led = led +1
            sleep(0.001)
    return leds            

#------------------------ Functions for Animation 4(Sun Rise and Dawn)-------------------
def SunRiseDawn():
    led = 0
    while led<60:
        for rows in range(6):
            leds[led + rows*60] = (0,0,0)
        client.put_pixels(leds)
        led = led +1
    sleep(0.1)
    mountainGen()
    sunRise()
    sunDown()
    led = 0
    while led<60:
        for rows in range(6):
            leds[led + rows*60] = (0,0,0)
            client.put_pixels(leds)
        led = led +1   


def mountainGen():
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
    for led in range(6):
        leds[27+led]=(255,255,255)
        leds[87+led]=(255,255,255)
        leds[147+led]=(255,255,255)
        leds[207+led]=(255,255,255)
        leds[267+led]=(255,255,255)
        leds[327+led]=(255,255,255)
        client.put_pixels(leds)
        sleep(0.01)
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

     
def sunRise():
    global counter
    counter = 0
    while counter <3:
        for led in range(2):
            leds[254+led] = (255,0,0)
            client.put_pixels(leds)
            sleep(0.1)
            led = led + 1
        for led in range(4):
            leds[193+led] = (255,77,0)
            client.put_pixels(leds)
            sleep(0.1)
            led = led + 1
        for led in range(6):
            leds[132+led] = (255,103,0)
            client.put_pixels(leds)
            sleep(0.1)
            led = led + 1
        for led in range(8):
            leds[71+led] = (255,129,0)
            client.put_pixels(leds)
            sleep(0.1)
            led = led + 1
        for led in range(10):
            leds[10+led] = (255,167,0)
            client.put_pixels(leds)
            sleep(0.1)
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
            sleep(0.1)
            led = led + 1
        for led in range(8):
            leds[101+led] = (255,77,0)
            client.put_pixels(leds)
            sleep(0.1)            
            led = led + 1
        for led in range(6):
            leds[162+led] = (255,103,0)
            client.put_pixels(leds)
            sleep(0.1)
            led = led + 1
        for led in range(4):
            leds[223+led] = (255,129,0)
            client.put_pixels(leds)
            sleep(0.1)
            led = led + 1           
        for led in range(2):
            leds[284+led] = (255,167,0)
            client.put_pixels(leds)
            sleep(0.1)
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
        counter = counter +1
       
#-----------------------------Animation 5 (FireWorks)-------------------------#
def fireWorks():
    leds=[(0,0,0)]*360
    client.put_pixels(leds)
    Fcounter = 0
    while True:
        randExplosion = random.randint(0,3)
        Fhappened= False
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

Welcome()
#-----------------------GUI---------------------------------
window=tk.Tk()
window.title('Animations by Brendan')
window.geometry("500x100")
window.resizable(0,0)
#-----------------Grid configuration-----------------------
window.columnconfigure(0, weight =2)
window.columnconfigure(1, weight =2)
window.columnconfigure(2, weight =2)
window.columnconfigure(3, weight =2)
window.columnconfigure(4, weight =2)
window.columnconfigure(5, weight =2)
window.rowconfigure(1, weight =2)
window.rowconfigure(2, weight =2)
#-------------------------Text & button---------------------------------
Flabel = tk.Label(window, text = "Welcome to my Animation!")
#Creating a button for animation 1
animationButton1 = tk.Button(window, text = 'Vortex', command=vortex, fg="red")
#Creating a button for animation 2
animationButton2 = tk.Button(window, text = 'Year2022', command=year2022, fg="orange")
#Creating a button for animation 3
animationButton3 = tk.Button(window, text = 'RainDrop', command = rainDrop, fg="purple")
#Creating a button for animation 4
animationButton4 = tk.Button(window, text = 'SunRise&Dawn', command = SunRiseDawn, fg="green")
#Creating a button for animation 5
animationButton5 = tk.Button(window, text = 'Fireworks', command = fireWorks, fg="blue")
#Creating a button for exit(to terminate the GUI)
exit_button = tk.Button(window, text = 'Exit', command = window.destroy , fg="violet") 
#--------------Format---------------------------------------------------
Flabel.grid(column =2, row = 0)
animationButton1.grid(column = 0, row = 1, padx = 5, pady = 1)
animationButton2.grid(column = 1, row = 1, padx = 5, pady = 1)
animationButton3.grid(column = 2, row = 1, padx = 5, pady = 1)
animationButton4.grid(column = 3, row = 1, padx = 5, pady = 1)
animationButton5.grid(column = 4, row = 1, padx = 5, pady = 1)
exit_button.grid(column = 5, row = 7, sticky='e', padx = 5, pady = 5)

window.mainloop()
