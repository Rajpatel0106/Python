print("No 1 For Xerox")
print("No 2 For Type")
op = int(input("Enter Number ="))

if op == 1:
    qt = int(input("How many Pages ="))
    if qt > 50:
        bill = qt * 5
        print("Price = 5, Total Bill =", bill)
    else:
        bill1 = qt * 7
        print("Price = 7, Total Bill =", bill1)
elif op == 2:
    qt1 = int(input("How many Words ="))
    if qt1 > 50:
        bill = qt1 * 15
        print("Price = 15, Total Bill =", bill)
    else:
        bill1 = qt1 * 20
        print("Price = 20, Total Bill =", bill1)
else:
    print("Wrong option")
