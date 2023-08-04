import time
import datetime

print(" Current date and time :",time.strftime("%Y-%m-%d %H:%M:%S"))
print(" Current year :", time.strftime("%Y"))
print(" Month of year :", time.strftime("%B"))
print(" Week number of the year :",time.strftime("%V"))
print(" Weekday of the week :",datetime.datetime.now().isoweekday())
print(" Day of year :",datetime.datetime.now().strftime("%j"))
print(" Day of the month :",datetime.datetime.now().strftime("%d"))
print(" Day of week :",datetime.datetime.now().strftime("%A"))
