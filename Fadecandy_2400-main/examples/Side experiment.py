import opc
import time

leds=[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0

while led < 60:
    for rows in range (6):
        leds[led + rows*60] = (255,0,0)
        
    time.sleep(.1)
    client.put_pixels(leds)
    led = led +1
    
led = 0

while led < 60:
    for rows in range (6):
        
        leds[3 + rows*60] = (0,0,255)
    time.sleep(.1)
    client.put_pixels(leds)
    led = led +1
