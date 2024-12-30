# Current Year is leap year?
import time
current = time.localtime(time.time())
if current.tm_year % 4 == 0:
    print("leap year")
else:
    print("Not Leap")