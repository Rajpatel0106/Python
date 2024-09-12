# 1 + 2 + 9 + 16 + 125 +

no = int(input("Enter No ="))

for i in range(1, no + 1):
    if i % 2 == 0:
        print(i * i, end=" + ")
    else:
        print(i * i * i, end=" + ")
