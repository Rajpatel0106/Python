# 4.Print Sum of even and Count also
t4=(11, 22, 33, 44, 55, 66, 99)
t = 0
c = 0
for i in t4:
    if i % 2 == 0:
        print(end="")
        t = t + i
        c = c + 1
print("\nTotal =", t)
print("Count =", c)

