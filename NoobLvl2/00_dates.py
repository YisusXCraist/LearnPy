### Dates ###
# Python has a module named datetime to work with dates as date objects.
# Import the datetime module and display the current date:

from datetime import datetime

now = datetime.now() # The datetime.now() method returns the current date and time.


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

current_time = time(21,6,0) # object of time class with hour, minute, second as arguments

print(current_time.hour)
print(current_time.minute)
print(current_time.second) 

from datetime import date

current_date = date(1970,3,1 ) # object of date class with year, month, day as arguments

print(current_date.year)
print(current_date.month)
print(current_date.day)
 
current_date = date.today() # object of date class with year, month, day as arguments! Today's date

print(current_date.year)
print(current_date.month)
print(current_date.day)

#current_date.year += 1 # This will not work because date objects are immutable
current_date = date(current_date.year + 1, current_date.month, current_date.day) # This will work

print(current_date.year)

diff = current_date - date(1970,3,1) # This will work because date objects are immutable and we can subtract them
print(diff.days) # 18262


from datetime import timedelta

#time_delta= timedelta(days=1, hours=2, minutes=3, seconds=4) # days, seconds, microseconds, milliseconds, minutes, hours, and weeks.
start_timedelta = timedelta(days=1, hours=2, minutes=3, seconds=4, weeks=15) 
end_timedelta =  timedelta(days=2, hours=3, minutes=4, seconds=5, weeks=13)

print(start_timedelta.days - end_timedelta.days) 