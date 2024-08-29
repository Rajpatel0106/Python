NO1 = int(input("Enter Number1 ="))
No2 = int(input("Enter Number2 ="))
No3 = int(input("Enter Number3 ="))

if NO1 > No2 and NO1 > No3:
    print("No1 Is Largest")
elif No2 > No3 and No2 > NO1:
    print("No2 Is Largest")
elif No3 > NO1 and No3 > No2:
    print("No3 Is Largest")
else:
    print("Wrong")
