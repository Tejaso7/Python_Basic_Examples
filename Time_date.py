import time
import datetime

#print(datetime.date.today().strftime())

print(time.time()) #timeStamp (epoch time)
now_1=datetime.datetime.now()
time_stamp = datetime.datetime.timestamp(now_1)

from datetime import date
today = date.today()
print("Today's date:", today)

import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
# display the calendar
print(calendar.month(yy, mm))
