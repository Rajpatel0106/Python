while True:
    print("Press 1 for square")
    print("Press 2 for cube")
    print("Press 3 for exit")
    op = int(input("Enter option ="))
    if op == 1:
        no = int(input("Enter Number = "))
        print("Square  =", no * no)
    elif op == 2:
        no = int(input("Enter Number = "))
        print("Cube =", no * no * no)
    elif op == 3:
        print("Bye")
        break
    else:
        print("Wrong opt")
