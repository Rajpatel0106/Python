# 12Hour format
import time
current = time.localtime(time.time())
if current.tm_hour >= 0 and current.tm_hour < 12:
    print(current.tm_hour)
else:
    print(current.tm_hour - 12)