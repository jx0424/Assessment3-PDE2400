import opc
from time import sleep
import random

leds=[(0,0,0)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

def PokemonQuiz():
    print("----------Welcome to Pokemon type challenge----------")
    randQuestion=random.randint(0,9)
    #---------------------------List of typing---------------------
    list1=['water','Water','WATER']
    list2=['fire','Fire','FIRE']
    list3=['grass','Grass','GRASS']
    list4=['normal','Normal','NORMAL']
    list5=['electric','Electric','ELECTRIC']
    list6=['ice','Ice','ICE']
    list7=['fighting','Fighting','FIGHTING']
    list8=['poison','Poison','POISON']
    list9=['ground','Ground','GROUND']
    list10=['flying','FLYING','Flying']
    list11=['pychic','Pychic','PYCHIC']
    list12=['bug','Bug','BUG']
    list13=['rock','Rock','ROCK']
    list14=['ghost','Ghost','GHOST']
    list15=['dragon','Dragon','DRAGON']
    list16=['Dark','dark','DARK']
    list17=['Steel','steel','STEEL']
    list18=['Fairy','fairy','FAIRY']
    #---------------Questions--------------------------
    if randQuestion==1:
        Question1=input("Which type is stronger than the other? Normal or Fighting: ")
        while Question1 not in list7 or Question1 not in list4:
            if Question1 in list7:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question1 in list4:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question1=input("Please enter a valid answer: ")
            
    if randQuestion==2:
        Question2=input("Which type is stronger than the other? Fire or Grass: ")
        while Question2 not in list2 or Question2  not in list3:
            if Question2 in list2:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question2 in list3:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question2= input("Please enter a valid answer: ")

    if randQuestion==3:
        Question3=input("Which type is stronger than the other? Water or Electric: ")
        while Question3 not in list5 or Question3 not in list1:
            if Question3 in list5:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question3 in list1:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question3= input("Please enter a valid answer: ")
                
    if randQuestion==4:
        Question4=input("Which type is stronger than the other? Dragon or Fairy: ")
        while Question4 not in list18 or Question4 not in list15:
            if Question4 in list18:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question4 in list15:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question4= input("Please enter a valid answer: ")
                
    if randQuestion==5:    
        Question5=input("Which type is stronger than the other? Dark or Bug: ")
        while Question5 not in list16 or Question5 not in list12:
            if Question5 in list12:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question5 in list16:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question5= input("Please enter a valid answer: ")
                
    if randQuestion==6:
        Question6=input("Which type is stronger than the other? Flying or Rock: ")
        while Question6 not in list13 or Question6 not in list10:
            if Question6 in list13:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question6 in list10:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question6= input("Please enter a valid answer: ")
                
    if randQuestion==7:
        Question7=input("Which type is stronger than the other? Poison or Ground: ")
        while Question7 not in list9 or Question7 not in list8:
            if Question7 in list9:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question7 in list8:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question7= input("Please enter a valid answer: ")
        
    if randQuestion==8:
        Question8=input("Which type is stronger than the other? Ghost or Dark: ")
        while Question8 not in list16 or Question8 not in list14:
            if Question8 in list16:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question8 in list14:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question8= input("Please enter a valid answer: ")
                
    if randQuestion==9:
        Question9=input("Which type is stronger than the other? Pychic or Dark: ")
        while Question9 not in list16 or Question9 not in list11:
            if Question9 in list16:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question9 in list11:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question9= input("Please enter a valid answer: ")

    if randQuestion==10:
        Question10=input("Which type is stronger than the other? Ice or Steel: ")
        while Question10 not in list17 or Question10 not in list6:
            if Question10 in list17:
                print("Your answer is ... CORRECT!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (0,255,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            elif Question10 in list6:
                print("Your answer is ... WRONG!")
                led=0
                while led<60:
                    for rows in range(6):
                        leds[led + rows*60] = (255,0,0)
                        client.put_pixels(leds)
                    led = led +1
                break
            else:
                Question10= input("Please enter a valid answer: ")

PokemonQuiz()
