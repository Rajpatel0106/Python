t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
while True:
    print("\n1 For Pizza")
    print("2 For Sandwich")
    print("3 For Burger")
    print("4 For Dosa")
    print("5 For Vada-pav")
    print("6 For Bill & Close")
    op = int(input("Enter Number For Oder ="))
    if op == 1:
        print("Pizza, Price = 399₹")
        no = int(input("Enter qty of pizza ="))
        t1 = no * 399
        print("Your Bill of Pizza=", t1)
    elif op == 2:
        print("\nSandwich, Price = 99₹")
        no = int(input("Enter qty of Sandwich ="))
        t2 = no * 99
        print("Your Bill =", t2)
    elif op == 3:
        print("\nBurger, Price = 139₹")
        no = int(input("Enter qty of Burger ="))
        t3 = no * 139
        print("Your Bill =", t3)
    elif op == 4:
        print("\nDosa, Price = 50₹")
        no = int(input("Enter qty of Dosa ="))
        t4 = no * 50
        print("Your Bill =", t4)
    elif op == 5:
        print("\nVada-pav, Price = 30₹")
        no = int(input("Enter qty of Vada-pav="))
        t5 = no * 30
        print("Your Bill =", t5)
    elif op == 6:
        Total = t1 + t2 + t3 + t4 + t5
        print("\nTotal Bill =", Total)
        print("Come Back Soon")
        break
    else:
        print("Wrong option")
