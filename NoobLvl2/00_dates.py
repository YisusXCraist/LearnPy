### Dates ###
# Python has a module named datetime to work with dates as date objects.
# Import the datetime module and display the current date:

from datetime import datetime

now = datetime.now()

# The datetime.now() method returns the current date and time.

print(now) # 2020-05-01 15:10:00.000000
print(now.year) # 2020
print(now.month) # 5
print(now.day) # 1
print(now.hour) # 15
print(now.minute) # 10
print(now.second) # 0
print(now.microsecond) # 0

timestamp = now.timestamp()
print(timestamp) # 1588332200.0


year_2023 = datetime(2023, 4, 4)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)

print_date(year_2023) # 2023 4 4 0 0 0 0

from datetime import time

current_time = time(now.hour, now.minute, now.second, now.microsecond) 
print(current_time) # 15:10:00