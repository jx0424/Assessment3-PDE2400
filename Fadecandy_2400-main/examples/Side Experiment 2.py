from datetime import date
from datetime import time
from datetime import datetime

#to get the time and date from user's computer
def getDateTime():
    today_date = date.today()
    current_Time = datetime.now()
    print(today_date)
    print(current_Time)

#just to test and print out the outcome
if __name__ == "__main__":
    getDateTime();
    
