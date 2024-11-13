while True:
    print("option 1  for Cube")
    print("option 2  for Square")
    print("option 3  for Exit")
    op = int(input("Enter Number ="))
    if op == 1:
        no = int(input("Enter Number ="))
        print("Cube =", no*no*no)
    elif op == 2:
        no = int(input("Enter Number ="))
        print("Sq =",no*no)
    elif op==3:
        print("Bye")
        break
    else:
        print("Wrong opt")
