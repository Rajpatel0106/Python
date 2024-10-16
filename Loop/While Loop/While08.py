while True:
    print("Press 1 for Sum")
    print("Press 2 for Sub")
    print("Press 3 for Mul")
    print("Press 4 for Div")
    print("Press 5 for Exit")
    op = int(input("Enter option ="))
    if op == 1:
        no1 = int(input("Enter Number1 ="))
        no2 = int(input("Enter Number2 ="))
        print("Sum =", no1 + no2)
    elif op == 2:
        no1 = int(input("Enter Number1 ="))
        no2 = int(input("Enter Number2 ="))
        print("Sub =", no1 - no2)
    elif op == 3:
        no1 = int(input("Enter Number1 ="))
        no2 = int(input("Enter Number2 ="))
        print("Mul =", no1 * no2)
    elif op == 4:
        no1 = int(input("Enter Number1 ="))
        no2 = int(input("Enter Number2 ="))
        print("Div =", no1 / no2)
    elif op == 5:
        print("come back soon")
        break
    else:
        print("wrong option")
