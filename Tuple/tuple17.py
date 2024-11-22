# 5.Display only numbers divisible by 7 , count and sum it
t5=(11, 21, 33, 42, 55, 63, 99)
t = 0
c = 0
for i in t5:
    if i % 7 == 0:
        print(i, end=", ")
        t = t + i
        c = c + 1
print("\nTotal =", t)
print("Count =",c)
