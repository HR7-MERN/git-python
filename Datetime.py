from datetime import time
from datetime import date
import datetime
date_obj = datetime.date(1998, 5, 2)
print(date_obj)
date_obj1 = datetime.date.today()  # To print todays date.
print(date_obj1)
# Accessing the attributes of the date of object.
print(date_obj.year)
print(date_obj.month)
print(date_obj.day)
date_obj2 = date(2019, 4, 16)
print(date_obj2)

time_obj = time(11, 59, 00)
print(time_obj)
