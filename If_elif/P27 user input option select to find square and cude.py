print("Press 1 for square")
print("Press 2 for cube")
op = int(input("Enter option =>"))

if op == 1:
    No1 = int(input("Enter Number ="))
    sq = No1 * No1
    print("Square =", sq)
elif op == 2:
    No1 = int(input("Enter Number ="))
    cu = No1 * No1 * No1
    print("Cube =", cu)
else:
    print("Wrong opt")
