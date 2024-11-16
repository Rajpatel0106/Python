List = [11, 44, 500, 22, 99, 77, 200, 66, 2]
c1 = 0
c2 = 0
for i in List:
    if i % 2 == 0:
        print(i, end=" ")
        c1 = c1 + 1
    else:
        print(i, end=" ")
        c2 = c2 + 1

print("\nTotal even are = ", c1)
print("Total even are = ", c2)
