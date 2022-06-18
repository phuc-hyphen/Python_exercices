import random
import math
from datetime import *

print(random.randrange(0, 200))

print("Arrondi supérieure of 3.6: ", math.ceil(3.6))
print("Arrondi inférieure of 3.6: ", math.floor(3.6))

print("Arrondi décimal: ", round(3.67876, 3))

print(datetime(2000, 1, 1))  # 2000-01-01 00:00:00

print(datetime.now())  # 2022-01-17 17:33:23.433535
print(datetime.now().time())  # 17:33:23.433535
print(datetime.now().year)  # 2022
print(datetime.now().month)  # 1
print(datetime.now().day)  # 17
print(datetime.now().hour)  # 17
print(datetime.now().minute)  # 35
print(datetime.now().second)
print(datetime.now().microsecond)
print(datetime.now() - datetime(2000, 1, 1))  # 8052 days, 17:33:23.433535
print(datetime.now() + timedelta(days=15))  # 2022-02-01 17:33:23.433535

print("formatage: ", datetime.now().strftime("%Y-%m-%d %H:%M"))

print("Current year: ", datetime.now().strftime("%Y"))
print("Month of year: ", datetime.now().strftime("%B"))
print("Week number of the year: ", datetime.now().strftime("%W"))
print("Weekday of the week: ", datetime.now().strftime("%w"))
print("Day of year: ", datetime.now().strftime("%j"))
print("Day of the month : ", datetime.now().strftime("%d"))
print("Day of week: ", datetime.now().strftime("%A"))
