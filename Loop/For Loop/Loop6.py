# -1 + 2 -3 + 4 - 5

no = int(input("Enter No ="))

for i in range(1, no + 1):
    if i % 2 == 0:
        print(+i, end=" ")
    else:
        print(-i, end=" + ")
