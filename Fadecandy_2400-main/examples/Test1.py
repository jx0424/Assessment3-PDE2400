import opc
import time
import random

#Creating a white background
leds=[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
