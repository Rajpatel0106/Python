# 1 + 3 + 5 +7 + 9+ 11

no = int(input("Enter No ="))

for i in range(1, no + 1):
    if i % 2 != 0:
        print(i, end=" + ")
