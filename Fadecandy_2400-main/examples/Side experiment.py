import opc
import time

leds=[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)



#while led < 60:
   # for rows in range (6):
    #    leds[led + rows*60] = (255,0,0)
    #time.sleep(.1)
    #client.put_pixels(leds)
   # led = led +1
leds[10]=(0,255,0)
client.put_pixels(leds)
