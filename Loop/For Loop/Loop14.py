# 1 + 8 + 27 +64+ 125+

no = int(input("Enter No ="))
t = 0
for i in range(1, no + 1):
    print(i*i*i, end=" + ")
    t = t + i*i*i
print("Total =", t)
