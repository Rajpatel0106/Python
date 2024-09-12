# 1 + 4 + 9 + 16 + 125 +

no = int(input("Enter No ="))
t = 0
for i in range(1, no + 1):
    if i % 2 == 0:
        print(i * i, end=" + ")
        t = t + i * i
    else:
        print(i*i*i, end=" + ")
        t = t + i * i * i
print("Total =", t, end="")
