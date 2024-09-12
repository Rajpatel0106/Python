# 1 + 4 + 9 + 16 + 25 +

no = int(input("Enter No ="))
c = 0
for i in range(1, no + 1):
    print(i * i, end=" + ")
    c = c + i * i
print("Total =", c, end="")
