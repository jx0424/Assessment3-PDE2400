value = input("Welcome to the menu. Options are listed below: \n\t 1. Roll \n\t 2.Sweep \n\t 3. Scroll \n Type the numbers of your choice:") #\n-new line \t-tab

#print("The value you input is:", value)
#print(f'it is of type{type(value)}.')

while True:
    if value.isdigit()== True: # .isdigit() is to check if the input is a digit
        value = int(value)
        break #exit the loop when the correct data type is enterd.
    else:
        value = input("Invalid input, please provide an integer:") #ask user to reenter value
        
#print("The converted value is:", value)
#print(f'it is of type{type(value)}.')


if value == 1:
    func1(value)
elif value ==2:
    func2(value)
elif value ==3:
    func3(value)

