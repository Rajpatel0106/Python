print("No 1 For Xerox")
print("No 2 For Type")
print("No 3 For Both")
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
    qt = int(input("How many Words ="))
    if qt > 50:
        bill = qt * 15
        print("Price = 15, Total Bill =", bill)
    else:
        bill1 = qt * 20
        print("Price = 20, Total Bill =", bill1)
elif op == 3:
    qt1 = int(input("How many Pages ="))
    qt2 = int(input("How many Word ="))

    if qt1 > 50:
        bill = qt1 * 5
        print("Price = 5, Total Bill =", bill)
    else:
        bill = qt1 * 7
        print("Price = 7, Total Bill =", bill)

    if qt2 > 50:
        bill1 = qt2 * 15
        print("Price = 15, Total Bill =", bill1)
    else:
        bill1 = qt2 * 20
        print("Price = 20, Total Bill =", bill1)

    Total = bill + bill1
    print("Total Bill =", Total)
else:
    print("Wrong option")
