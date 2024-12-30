# Good morning , Good Evening , Good Night
import time
current = time.localtime(time.time())
if current.tm_hour < 12:
    print("Good Morning")
elif  current.tm_hour < 18:
    print("Good Afternoon")
elif  current.tm_hour < 20:
    print("Good Evening")
elif  current.tm_hour < 6:
    print("Good Night")

 # current.tm_hour > 6 and
# current.tm_hour > 12 and
# current.tm_hour > 18 and
# current.tm_hour > 20 and