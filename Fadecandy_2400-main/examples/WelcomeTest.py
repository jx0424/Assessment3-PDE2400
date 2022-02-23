import opc
from time import sleep

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

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












    
