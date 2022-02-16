from datetime import date
from datetime import time
from datetime import datetime

#to get the date from user's computer
def getDateTime():
    today_year = date.today().year
    print(today_year)

#just to test and print out the outcome
if __name__ == "__main__":
    getDateTime();
    
