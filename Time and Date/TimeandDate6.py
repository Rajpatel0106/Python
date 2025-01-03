#How much time to wait for press enter is show in output.?
import time
now = time.time()
a=input("Enter name =>")
later = time.time()
difference = int(later - now)
print(difference)
