print("Press 1 For Battery-Based Toys")
print("Press 2 For Key-based Toys")
print("Press 3 For Electrical Charging Based Toys")

No = int(input("Enter Number ="))

if No == 1:

    No1 = int(input("Enter Amount ="))
    if No1 > 1000:
        dis = No1 * 10 / 100
        dis1 = No1 - No1 * 10 / 100
        print("Your Discount =", dis)
        print("Your Bill =", dis1)
    else:
        print("Your Bill =", No1)

elif No == 2:

    No1 = int(input("Enter Amount ="))
    if No1 > 100:
        dis = No1 * 5 / 100
        dis1 = No1 - No1 * 5 / 100
        print("Your Discount =", dis)
        print("Your Bill =", dis1)
    else:
        print("Your BIll =", No1)

elif No == 3:

    No1 = int(input("Enter Your Amount ="))
    if No1 > 500:
        dis = No1 * 10 / 100
        dis1 = No1 - No1 * 10 / 100
        print("Your Discount =", dis)
        print("Your Bill =", dis1)
    else:
        print("Your Bill =", No1)

else:
    print("Wrong input")
