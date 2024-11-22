# 7.Print 11 -22 33 -44 55 in reverse -11 22 -33 44 -55
t7=(11, 22, 33, 44, 55, 66, 99)
for i in t7:
    if i % 2 == 0:
        print(-i, end=", ")
    else:
        print(i,end=", ")

for x in t7:
    if x % 2 == 0:
        print(x, end=", ")
    else:
        print(-x,end=", ")
