unit = int(input("Enter Unit ="))
free = unit - 300

if unit <= 100:
    print("Free")
elif 100 < unit <= 300:
    charge = 2 * (unit - 100)
    print("Rs 2 Per Day", charge)
elif unit > 300:
    bill = 2 * 200
    bill1 = 5 * (unit - 300)
    print("Rs 2 Per Day", bill)
    print("Rs 5 Per Day", bill1)
    total = bill + bill1
    print("Total Bill =", total)
else:
    print("wrong")
