dis = int(input("Enter distance (km) ="))
wei = int(input("Enter weight (kg) ="))

if dis <= 100 and wei <= 5:
    print("Standard Shipping")
elif dis > 100 and wei <= 5:
    print("Express Shipping")
elif wei > 5:
    print("Freight Shipping")
else:
    print("Wrong")
