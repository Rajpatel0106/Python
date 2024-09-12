n = int(input("en no ="))
for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print("T,F")
    elif i % 3 == 0:
        print("T")
    elif i % 5 == 0:
        print("F")
    else:
        print(i)
        