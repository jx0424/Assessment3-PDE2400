import opc
import time
import random

#Creating a white background
leds=[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#-----------------User input-------------------#
user_Input = input ("Please select one of the options below: \n\t 1.Tic Tac Toe \n\t 2.RGB lights \n\t 3.Malaysia Flag \n Type the number of your choice:")

while True:
    if user_Input.isdigit() == True: #To check if the user's input is digit
        user_Input = int (user_Input)
        if user_Input > 6 or user_Input < 1: #To prevent user from entering value that is out of range 
            user_Input = input ("Please enter the number between 1 and 6 only:")
            continue #This will skip the rest of the loop and start at user_Input.isdigit to check if the input is digit.
        else:
            break #To exit the loop when appropriate input is entered.
    else:
        user_Input = input ("Please only retype a number:") #If user enter anything other than numbers, this will prompt and ask user to input number only.

#--------------Fuction definitions------------#
def rgb_func():
    led = 0
    while led<60: #scroll through all rows at the same time
        for rows in range(6):
            leds[led + rows*60] = (0,0,255)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led + 1
    
#Performing the functions base on user's input.
if user_Input == 1:
    rgb_func()
elif user_Input == 2:
    print (user_Input)
elif user_Input == 3:
    print (user_Input)
elif user_Input == 4:
    print (user_Input)
elif user_Input == 5:
    print (user_Input)
elif user_Input == 6:
    print (user_Input)
