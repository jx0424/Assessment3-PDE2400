import opc
import random
import time
import colorsys
from datetime import date

#create a function for first animation(vortex)
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

#to get the time and date from user's computer
def getDateTime():
    today_year = date.today().year
    print(today_year)


#create a function for second animation
#def year_printer():

        
#call function
#vortex()
getDateTime()
